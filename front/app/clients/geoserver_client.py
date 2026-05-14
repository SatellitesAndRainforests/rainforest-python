import requests


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


def publish_context_package_stub(
        workspace: str,
        context_package_id: str,
        layer: str ) -> dict:

    safe_layer = layer.lower().replace(":", "_").replace("-", "_")

    geoserver_layer_name = f"{workspace}:context_{context_package_id[:8]}_{safe_layer}"

    return {
        "status": "PUBLISHED",
        "geoserverLayerName": geoserver_layer_name,
        "geoserverWmsUrl": f"/geoserver/{workspace}/wms",
        "errorMessage": None,
    }


