import requests


def create_context_package( base_url: str, payload: dict ) -> dict:

    response = requests.post(
            f"{base_url}/context-packages",
            json = payload,
            timeout = 10,
    )

    response.raise_for_status()
    
    return response.json()




