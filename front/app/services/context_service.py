from flask import current_app

from app.clients.nasa_api_client import build_nasa_gibs_preview_url


def build_context_request(latitude: float, longitude: float) -> dict:

    nasa_preview_url = build_nasa_gibs_preview_url(
        latitude = latitude,
        longitude = longitude,
        endpoint = current_app.config["NASA_GIBS_WMS_ENDPOINT"],
        layer = current_app.config["NASA_GIBS_DEFAULT_LAYER"]
    )

    return {
        "latitude": latitude,
        "longitude": longitude,
        "nasa_preview_url": nasa_preview_url
    }


