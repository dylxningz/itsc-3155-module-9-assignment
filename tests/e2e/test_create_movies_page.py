import pytest
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_create_movie(client):
    response = client.post('/movies', data={
        'title': 'Test Movie',
        'director': 'Test Director',
        'rating': '5'
    })

    assert response.status_code == 302

    response = client.get('/movies')

    assert b'Test Movie' in response.data
