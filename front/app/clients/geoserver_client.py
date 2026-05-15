from pathlib import Path
import requests
from app.services.gdal_service import build_nasa_layer_base_name


def check_geoserver_connection(
        base_url: str,
        username: str,
        password: str) -> dict:

    response = requests.get(
        f"{base_url}/rest/workspaces.json",
        auth = (username, password),
        timeout = 10,
    )

    response.raise_for_status()

    return response.json()


def publish_context_package(
        base_url: str,
        username: str,
        password: str,
        workspace: str,
        context_package_id: str,
        geotiff_path: Path) -> dict:

    layer_base_name = build_nasa_layer_base_name(context_package_id)

    upload_url = (
        f"{base_url}/rest/workspaces/{workspace}/coveragestores/"
        f"{layer_base_name}/file.geotiff?configure=first"
    )

    with open(geotiff_path, "rb") as geotiff_file:
        response = requests.put(
            upload_url,
            auth=(username, password),
            headers={"Content-type": "image/tiff"},
            data=geotiff_file,
            timeout=120,
        )

    response.raise_for_status()

    return {
        "status": "PUBLISHED",
        "geoserverLayerName": f"{workspace}:{layer_base_name}",
        "geoserverWmsUrl": f"/geoserver/{workspace}/wms",
        "errorMessage": None,
    }


