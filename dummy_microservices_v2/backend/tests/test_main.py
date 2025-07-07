import pytest
from fastapi.testclient import TestClient
from app.main import BackendApp
from unittest.mock import patch

@pytest.fixture
def client():
    backend_app = BackendApp()
    return TestClient(backend_app.app)

@patch('app.main.AuthService.verify_token')
@patch('app.main.ISSService.get_iss_position_with_location')
def test_iss_success(mock_iss, mock_auth, client):
    mock_auth.return_value = {'user_id': 1}
    mock_iss.return_value = {
        'latitude': '10.0',
        'longitude': '20.0',
        'location_type': 'country',
        'location_name': 'Testland'
    }
    headers = {"Authorization": "Bearer testtoken"}
    response = client.get("/iss", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data['latitude'] == '10.0'
    assert data['longitude'] == '20.0'
    assert data['location_type'] == 'country'
    assert data['location_name'] == 'Testland'

@patch('app.main.AuthService.verify_token')
def test_iss_unauthorized(mock_auth, client):
    mock_auth.return_value = None
    headers = {"Authorization": "Bearer badtoken"}
    response = client.get("/iss", headers=headers)
    assert response.status_code == 401
    assert response.json()['detail'] == 'Invalid or expired token' 