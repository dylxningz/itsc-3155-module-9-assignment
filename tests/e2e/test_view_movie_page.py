from app import app
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository


def test_get_movie_by_its_id():
    # Creates a testing movie object
    test_movie = Movie(movie_id=1, title='Test Movie', director='Test Director', rating=1)



    movie_repo = get_movie_repository()



    movie_repo._db[1] = test_movie       # add test movie to db

    with app.test_client() as client:
        response = client.get('/movies/1')  # test get request to the specific movie id




        assert response.status_code == 200
        assert b'Test Movie' in response.data
        assert b'Test Director' in response.data