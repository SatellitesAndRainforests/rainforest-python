# app/services/gdal_service.py

from pathlib import Path
import subprocess

import requests


def parse_bbox(bbox: str) -> tuple[float, float, float, float]:
    parts = [float(part.strip()) for part in bbox.split(",")]

    if len(parts) != 4:
        raise ValueError(f"bbox must contain 4 values: {bbox}")

    min_lon, min_lat, max_lon, max_lat = parts
    return min_lon, min_lat, max_lon, max_lat


def make_safe_geoserver_id(context_package_id: str) -> str:
    return context_package_id.replace("-", "_")


def build_nasa_layer_base_name(context_package_id: str) -> str:
    safe_id = make_safe_geoserver_id(context_package_id)
    return f"context_{safe_id}_nasa"


def run_gdal_command(command: list[str]) -> None:
    try:
        subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as error:
        raise RuntimeError(
            "GDAL command failed:\n"
            f"Command: {' '.join(command)}\n"
            f"STDOUT: {error.stdout}\n"
            f"STDERR: {error.stderr}"
        ) from error


def download_file(url: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    response = requests.get(url, timeout=60)
    response.raise_for_status()

    output_path.write_bytes(response.content)


def convert_nasa_image_to_geotiff_for_geoserver(
    production_url: str,
    bbox: str,
    context_package_id: str,
    generated_dir: str = "generated",
) -> Path:
    layer_base_name = build_nasa_layer_base_name(context_package_id)

    generated_path = Path(generated_dir)
    jpg_path = generated_path / f"{layer_base_name}.jpg"
    tif_4326_path = generated_path / f"{layer_base_name}_4326.tif"
    tif_3857_path = generated_path / f"{layer_base_name}_3857.tif"

    min_lon, min_lat, max_lon, max_lat = parse_bbox(bbox)

    download_file(production_url, jpg_path)

    run_gdal_command([
        "gdal_translate",
        "-of", "GTiff",
        "-a_srs", "EPSG:4326",
        "-a_ullr",
        str(min_lon),
        str(max_lat),
        str(max_lon),
        str(min_lat),
        str(jpg_path),
        str(tif_4326_path),
    ])

    run_gdal_command([
        "gdalwarp",
        "-t_srs", "EPSG:3857",
        "-r", "bilinear",
        "-of", "GTiff",
        "-co", "TILED=YES",
        "-co", "BLOCKXSIZE=256",
        "-co", "BLOCKYSIZE=256",
        "-co", "COMPRESS=JPEG",
        "-co", "JPEG_QUALITY=85",
        "-co", "PHOTOMETRIC=YCBCR",
        "-co", "BIGTIFF=IF_SAFER",
        str(tif_4326_path),
        str(tif_3857_path),
    ])

    return tif_3857_path


def delete_generated_context_files(
    context_package_id: str,
    generated_dir: str = "generated",
) -> None:

    layer_base_name = build_nasa_layer_base_name(context_package_id)
    generated_path = Path(generated_dir)

    files_to_delete = [
        generated_path / f"{layer_base_name}.jpg",
        generated_path / f"{layer_base_name}_4326.tif",
        generated_path / f"{layer_base_name}_3857.tif",
    ]

    for file_path in files_to_delete:
        file_path.unlink(missing_ok=True)



