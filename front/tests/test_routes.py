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
