import requests


def create_context_package( base_url: str, payload: dict ) -> dict:

    response = requests.post(
            f"{base_url}/context-packages",
            json = payload,
            timeout = 10,
    )

    response.raise_for_status()
    
    return response.json()


def update_context_package_status(
        base_url: str,
        context_package_id: str,
        payload: dict ) -> dict:

    response = requests.patch(
        f"{base_url}/context-packages/{context_package_id}/status",
        json = payload,
        timeout = 10
    )

    response.raise_for_status()

    return response.json()




