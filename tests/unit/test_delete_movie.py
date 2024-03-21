import pytest
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def movie_repository():
    movie_repo = get_movie_repository()
    movie_repo.clear_db()

    return movie_repo
def test_delete_movie(movie_repo):

    movie = movie_repo.create_movie("Bocchi the Rock: Budokan", "Keiichiro Saito", 3)

    assert movie_repo.get_movie_by_id(movie.movie_id) is not None

    movie_repo.delete_movie(movie.movie_id)

    deleted_movie = movie_repo.get_movie_by_id(movie.movie_id)
    assert deleted_movie is None