from app import app


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

    def fake_create_context_package( base_url: str, payload: dict ) -> dict:
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

    def fake_update_context_package_status(
            base_url: str,
            context_package_id: str,
            payload: dict) -> dict:
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


