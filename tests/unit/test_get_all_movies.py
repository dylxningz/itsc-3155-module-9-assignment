import pytest
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def movie_repo():
    repo = get_movie_repository()
    repo.clear_db() 
    repo.create_movie("Inception", "Christopher Nolan", 5)
    repo.create_movie("Interstellar", "Christopher Nolan", 5)
    return repo

def test_get_all_movies(movie_repo):

    movies = movie_repo.get_all_movies()
    assert len(movies) == 2, "Expected exactly 2 movies to be retrieved"
    all_titles = [movie.title for movie in movies.values()]
    assert "Inception" in all_titles, "Inception should be in the list of movies"
    assert "Interstellar" in all_titles, "Interstellar should be in the list of movies"
