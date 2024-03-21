
from app import app
from unittest.mock import MagicMock

def test_get_single_movie_not_found():
    mock_repo = MagicMock()
    mock_repo.get_movie_by_id.return_value = None  

    with app.test_client() as client:
        response = client.get('/movies/2')  
        assert response.status_code == 404
        assert b'Movie not found' in response.data 
