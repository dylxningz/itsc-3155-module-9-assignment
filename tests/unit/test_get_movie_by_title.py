# TODO: Feature 3
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository


def test_get_movie_by_title():
    title = "The Godfather"
    director = "Francis Ford Coppola"
    rating = 2

    movie_repository = get_movie_repository()
    movie_repository.create_movie(title=title, director=director, rating=rating)

    assert movie_repository.get_movie_by_title("The Godfather") is not None
