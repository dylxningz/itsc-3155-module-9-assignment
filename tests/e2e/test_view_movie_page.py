from flask.testing import FlaskClient
import pytest
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository


def test_get_single_movie_valid_id(test_app:FlaskClient):
    repo = get_movie_repository()
    repo.create_movie(title="The Godfather", director="Francis Ford Coppola", rating=2)

    movie = repo.get_movie_by_title("The Godfather")
    
    response = test_app.get(f'/movies/{movie.movie_id}')
    assert response.status_code == 200
    assert b'movie' in response.data



