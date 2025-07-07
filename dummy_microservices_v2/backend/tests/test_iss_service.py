import pytest
from app.iss_service import ISSService
from unittest.mock import patch

@pytest.fixture
def service():
    return ISSService()

@patch('app.iss_service.requests.get')
def test_get_iss_position_success(mock_get, service):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "iss_position": {"latitude": "10.0", "longitude": "20.0"}
    }
    result = service.get_iss_position()
    assert result == {"latitude": "10.0", "longitude": "20.0"}
    mock_get.assert_called_once_with(service.ISS_API_URL, timeout=5)

@patch('app.iss_service.requests.get')
def test_get_location_info_country(mock_get, service):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"address": {"country": "Testland"}}
    result = service.get_location_info("10.0", "20.0")
    assert result == {"type": "country", "name": "Testland"}

@patch('app.iss_service.requests.get')
def test_get_location_info_sea(mock_get, service):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"address": {"sea": "Test Sea"}}
    result = service.get_location_info("10.0", "20.0")
    assert result == {"type": "sea", "name": "Test Sea"}

@patch('app.iss_service.requests.get')
def test_get_location_info_unknown(mock_get, service):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"address": {}}
    result = service.get_location_info("10.0", "20.0")
    assert result == {"type": "unknown", "name": "Unknown"}

@patch('app.iss_service.requests.get')
def test_get_location_info_exception(mock_get, service):
    mock_get.side_effect = Exception("API error")
    result = service.get_location_info("10.0", "20.0")
    assert result == {"type": "unknown", "name": "Unknown"}

@patch.object(ISSService, 'get_location_info')
@patch.object(ISSService, 'get_iss_position')
def test_get_iss_position_with_location(mock_pos, mock_loc, service):
    mock_pos.return_value = {"latitude": "10.0", "longitude": "20.0"}
    mock_loc.return_value = {"type": "country", "name": "Testland"}
    result = service.get_iss_position_with_location()
    assert result == {
        "latitude": "10.0",
        "longitude": "20.0",
        "location_type": "country",
        "location_name": "Testland"
    } 