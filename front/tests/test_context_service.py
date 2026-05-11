from app import app
from app.services.context_service import build_context_request

def test_build_context_request():

    with app.app_context():
        result = build_context_request(51.5, -0.1)

    assert result ["latitude"] == 51.5
    assert result ["longitude"] == -0.1
    assert "nasa_preview_url" in result
    assert "VIIRS_SNPP_CorrectedReflectance_TrueColor" in result["nasa_preview_url"]

