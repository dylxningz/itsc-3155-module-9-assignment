import pytest
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def movie_repository():
    movie_repository = get_movie_repository()
    yield movie_repository

    movie_repository.clear_db()

def test_create_movie(movie_repository):
    movie = movie_repository.create_movie('Test Movie', 'Test Director', 5)

    assert movie.title == 'Test Movie'
    assert movie.director == 'Test Director'
    assert movie.rating == 5

    assert movie_repository.get_movie_by_id(movie.movie_id) is not None
