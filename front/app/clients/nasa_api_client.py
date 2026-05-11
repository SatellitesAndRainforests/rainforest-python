from datetime import date, timedelta
from urllib.parse import urlencode


def build_box(latitude: float, longitude: float, half_degree: float = 10.0) -> str:
    min_lon = max(longitude - half_degree, -180)
    max_lon = min(longitude + half_degree, 180)
    min_lat = max(latitude - half_degree, -90)
    max_lat = min(latitude + half_degree, 90)

    return f"{min_lon},{min_lat},{max_lon},{max_lat}"


def build_nasa_gibs_preview_url(
    latitude: float,
    longitude: float,
    endpoint: str,
    layer: str,
    image_date: str | None = None,
) -> str:

    if image_date is None:
        image_date = (date.today() - timedelta(days=1)).isoformat()

    params = {
        "SERVICE": "WMS",
        "REQUEST": "GetMap",
        "VERSION": "1.1.1",
        "LAYERS": layer,
        "STYLES": "",
        "FORMAT": "image/jpeg",
        "SRS": "EPSG:4326",
        "BBOX": build_box(latitude, longitude),
        "WIDTH": 300, # 2048 for scientific 
        "HEIGHT": 300, # 1048 or which is 2km per pixel
        "TIME": image_date,
    }

    return f"{endpoint}?{urlencode(params)}"
