import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from iss import app

client = TestClient(app)

@patch("iss.requests.get")
def test_get_iss_position_success(mock_get):
    # Mock ISS position API response
    mock_iss_response = {
        "iss_position": {"latitude": "10.0", "longitude": "20.0"},
        "message": "success",
        "timestamp": 1234567890
    }
    # Mock reverse geocoding API response
    mock_country_response = {
        "address": {"country": "Testland"}
    }
    def side_effect(url, headers=None):
        if "open-notify" in url:
            class MockResp:
                status_code = 200
                def json(self):
                    return mock_iss_response
            return MockResp()
        elif "nominatim" in url:
            class MockResp:
                status_code = 200
                def json(self):
                    return mock_country_response
            return MockResp()
        else:
            raise ValueError("Unexpected URL")
    mock_get.side_effect = side_effect

    response = client.get("/iss")
    assert response.status_code == 200
    data = response.json()
    assert data["latitude"] == "10.0"
    assert data["longitude"] == "20.0"
    assert data["country"] == "Testland"

@patch("iss.requests.get")
def test_get_iss_position_iss_api_failure(mock_get):
    # Simulate ISS API failure
    class MockResp:
        status_code = 500
        def json(self):
            return {}
    mock_get.return_value = MockResp()
    response = client.get("/iss")
    assert response.status_code == 502
    assert response.json()["error"] == "Failed to fetch ISS position" 