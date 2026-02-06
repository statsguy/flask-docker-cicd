import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert "Hello from Flask!" in data['message']
    assert 'version' in data

def test_health(client):
    """Test health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_add(client):
    """Test add endpoint"""
    response = client.get('/add/5/3')
    assert response.status_code == 200
    assert response.json['result'] == 8
    assert response.json['operation'] == 'addition'

def test_subtract(client):
    """Test subtract endpoint"""
    response = client.get('/subtract/10/4')
    assert response.status_code == 200
    assert response.json['result'] == 6

def test_multiply(client):
    """Test multiply endpoint"""
    response = client.get('/multiply/6/7')
    assert response.status_code == 200
    assert response.json['result'] == 42
