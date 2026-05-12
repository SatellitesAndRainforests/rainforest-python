import hashlib
from uuid import uuid4

from flask import current_app

from app.clients.nasa_api_client import (
        build_box,
        build_nasa_gibs_preview_url,
        get_default_image_date
)


def build_context_request(latitude: float, longitude: float) -> dict:

    image_date = get_default_image_date()
    layer = current_app.config["NASA_GIBS_DEFAULT_LAYER"]

    nasa_preview_url = build_nasa_gibs_preview_url(
        latitude = latitude,
        longitude = longitude,
        endpoint = current_app.config["NASA_GIBS_WMS_ENDPOINT"],
        layer = layer,
        image_date = image_date,
        width = current_app.config["NASA_GIBS_PREVIEW_WIDTH"],
        height = current_app.config["NASA_GIBS_PREVIEW_HEIGHT"],
        half_degree = current_app.config["NASA_GIBS_HALF_DEGREE"]
    )

    return {
        "latitude": latitude,
        "longitude": longitude,
        "layer": layer,
        "image_date": image_date,
        "bbox": build_box(latitude, longitude, current_app.config["NASA_GIBS_HALF_DEGREE"]),
        "nasa_preview_url": nasa_preview_url
    }


def build_context_import_request(
        latitude: float,
        longitude: float,
        layer: str,
        image_date: str,
) -> dict:

    bbox = build_box(
        latitude,
        longitude,
        current_app.config["NASA_GIBS_HALF_DEGREE"]
    )

    idempotency_source = f"{layer}:{image_date}:{bbox}"
    idempotency_key = hashlib.sha256(idempotency_source.encode()).hexdigest()
    correlation_id = str(uuid4())

    production_url = build_nasa_gibs_preview_url(
        latitude = latitude,
        longitude = longitude,
        endpoint = current_app.config["NASA_GIBS_WMS_ENDPOINT"],
        layer = layer,
        image_date = image_date,
        width = current_app.config["NASA_GIBS_EXPORT_WIDTH"],
        height = current_app.config["NASA_GIBS_EXPORT_HEIGHT"],
        half_degree = current_app.config["NASA_GIBS_HALF_DEGREE"]
    )

    return {
        "status": "PENDING",
        "latitude": latitude,
        "longitude": longitude,
        "layer": layer,
        "image_date": image_date,
        "bbox": bbox,
        "correlation_id": correlation_id,
        "idempotency_key": idempotency_key,
        "production_url": production_url,
    }



