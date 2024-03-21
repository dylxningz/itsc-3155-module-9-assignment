from flask.testing import FlaskClient
import pytest
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def movie_repository():
    # Set up the movie repository
    repo = get_movie_repository()


    # Yield the repository to the test
    yield repo



def test_delete_movie_page(test_app: FlaskClient,movie_repository):

    movie = Movie(movie_id=1, title="Test Movie", director="Test Director", rating=5)
    movie_repository._db[1] = movie

    response = test_app.post(f'/movies/1/delete')

    assert response.status_code == 302

