import pytest
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository




def test_delete_movie():
    repo = get_movie_repository()

    
    repo.create_movie(title="The Godfather", director="Francis Ford Coppola", rating=2)
    movie = repo.get_movie_by_title("The Godfather")
    id = movie.movie_id


    repo.delete_movie(id)

    assert repo.get_movie_by_title("The Godfather") is None