from app import app
from pathlib import Path


def test_health(client):

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "UP"


def test_context_form_page_loads(client):

    response = client.get("/context/new")

    assert response.status_code == 200
    assert b"Request location context" in response.data


def test_context_from_valid_post(client):

    response = client.post("/context/new", data={
        "latitude": "51.5",
        "longitude": "-0.1"
        })

    assert response.status_code == 200
    assert b"Context request received" in response.data
    assert b"51.5" in response.data
    assert b"-0.1" in response.data


def test_context_from_invalid_latitude(client):

    response = client.post("/context/new", data={
        "latitude": "999",
        "longitude": "-0.1"
        })

    assert response.status_code == 200
    assert b"Request location context" in response.data


def test_context_import_valid_post(client, monkeypatch):

    def fake_create_context_package(base_url: str, payload: dict) -> dict:
        return {
            "contextPackageId": "test-context-package-id",
            "status": "PENDING",
            "correlationId": payload["correlationId"],
            "idempotencyKey": payload["idempotencyKey"],
            "geoserverLayerName": None,
            "geoserverWmsUrl": None,
            "errorMessage": None,
        }

    monkeypatch.setattr(
        "app.routes.context_routes.create_context_package",
        fake_create_context_package
    )

    def fake_convert_nasa_image_to_geotiff_for_geoserver(
            production_url: str,
            bbox: str,
            context_package_id: str,
    ) -> Path:
        return Path("generated/test-context-package-id_3857.tif")

    monkeypatch.setattr(
        "app.routes.context_routes.convert_nasa_image_to_geotiff_for_geoserver",
        fake_convert_nasa_image_to_geotiff_for_geoserver
    )

    def fake_publish_context_package(
            base_url: str,
            username: str,
            password: str,
            workspace: str,
            context_package_id: str,
            geotiff_path: Path,
    ) -> dict:
        return {
            "status": "PUBLISHED",
            "geoserverLayerName": "rainforest:context_test_context_package_id_nasa",
            "geoserverWmsUrl": "/geoserver/rainforest/wms",
            "errorMessage": None,
        }

    monkeypatch.setattr(
        "app.routes.context_routes.publish_context_package",
        fake_publish_context_package
    )

    def fake_update_context_package_status(
            base_url: str,
            context_package_id: str,
            payload: dict
    ) -> dict:
        return {
            "contextPackageId": context_package_id,
            "status": payload["status"],
            "correlationId": "test-correlation-id",
            "idempotencyKey": "test-idempotency-key",
            "geoserverLayerName": payload["geoserverLayerName"],
            "geoserverWmsUrl": payload["geoserverWmsUrl"],
            "errorMessage": payload["errorMessage"],
        }

    monkeypatch.setattr(
        "app.routes.context_routes.update_context_package_status",
        fake_update_context_package_status
    )

    response = client.post("/context/import", data={
        "latitude": "50.0",
        "longitude": "0.0",
        "layer": "VIIRS_SNPP_CorrectedReflectance_TrueColor",
        "image_date": "2026-05-10",
    })

    assert response.status_code == 200
    assert b"Context package requested" in response.data
    assert b"PUBLISHED" in response.data
    assert b"VIIRS_SNPP_CorrectedReflectance_TrueColor" in response.data
    assert b"rainforest:context_test_context_package_id_nasa" in response.data


def test_context_import_marks_failed_when_gdal_or_geoserver_fails(client, monkeypatch):

    def fake_create_context_package(base_url: str, payload: dict) -> dict:
        return {
            "contextPackageId": "test-context-package-id",
            "status": "PENDING",
            "correlationId": payload["correlationId"],
            "idempotencyKey": payload["idempotencyKey"],
            "geoserverLayerName": None,
            "geoserverWmsUrl": None,
            "errorMessage": None,
        }

    monkeypatch.setattr(
        "app.routes.context_routes.create_context_package",
        fake_create_context_package
    )

    def fake_convert_nasa_image_to_geotiff_for_geoserver(
            production_url: str,
            bbox: str,
            context_package_id: str,
    ) -> Path:
        raise RuntimeError("GDAL failed during test")

    monkeypatch.setattr(
        "app.routes.context_routes.convert_nasa_image_to_geotiff_for_geoserver",
        fake_convert_nasa_image_to_geotiff_for_geoserver
    )

    def fake_update_context_package_status(
            base_url: str,
            context_package_id: str,
            payload: dict
    ) -> dict:
        return {
            "contextPackageId": context_package_id,
            "status": payload["status"],
            "correlationId": "test-correlation-id",
            "idempotencyKey": "test-idempotency-key",
            "geoserverLayerName": payload["geoserverLayerName"],
            "geoserverWmsUrl": payload["geoserverWmsUrl"],
            "errorMessage": payload["errorMessage"],
        }

    monkeypatch.setattr(
        "app.routes.context_routes.update_context_package_status",
        fake_update_context_package_status
    )

    response = client.post("/context/import", data={
        "latitude": "50.0",
        "longitude": "0.0",
        "layer": "VIIRS_SNPP_CorrectedReflectance_TrueColor",
        "image_date": "2026-05-10",
    })

    assert response.status_code == 200
    assert b"Context package requested" in response.data
    assert b"FAILED" in response.data
    assert b"GDAL failed during test" in response.data