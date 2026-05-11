from urllib.parse import parse_qs, urlparse

from app.clients.nasa_api_client import build_box, build_nasa_gibs_preview_url


def test_build_box_default_regional_bbox():
    result = build_box(latitude=51.5, longitude=-0.1)

    assert result == "-10.1,41.5,9.9,61.5"


def test_build_box_clamps_to_world_bounds():
    result = build_box(latitude=85.0, longitude=175.0)

    assert result == "165.0,75.0,180,90"


def test_build_nasa_gibs_preview_url_contains_expected_wms_params():
    url = build_nasa_gibs_preview_url(
        latitude=51.5,
        longitude=-0.1,
        endpoint="https://example.com/wms",
        layer="VIIRS_SNPP_CorrectedReflectance_TrueColor",
        image_date="2026-05-10",
    )

    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    assert parsed.scheme == "https"
    assert parsed.netloc == "example.com"
    assert parsed.path == "/wms"

    assert params["SERVICE"] == ["WMS"]
    assert params["REQUEST"] == ["GetMap"]
    assert params["VERSION"] == ["1.1.1"]
    assert params["LAYERS"] == ["VIIRS_SNPP_CorrectedReflectance_TrueColor"]
    assert params["FORMAT"] == ["image/jpeg"]
    assert params["SRS"] == ["EPSG:4326"]
    assert params["BBOX"] == ["-10.1,41.5,9.9,61.5"]
    assert params["WIDTH"] == ["300"]
    assert params["HEIGHT"] == ["300"]
    assert params["TIME"] == ["2026-05-10"]
