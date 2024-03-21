from app import app, get_single_movie
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository



test_movie = Movie(movie_id=1, title='Test Movie', director='Test Director', rating=1)



movie_repo = get_movie_repository()



movie_repo._db[1] = test_movie       # add test movie to db


def test_get_single_movie_valid_id():
    with app.test_client() as client:
        response = client.get('/movies/1')
        assert response.status_code == 200
        assert b'Test Movie' in response.data



