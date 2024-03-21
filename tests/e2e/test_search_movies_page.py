from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository



def test_search_movies_page(test_app:FlaskClient):
    

    response = test_app.get('/movies/search')
    response_data = response.data.decode('utf-8')
    post = test_app.post('/movies/search', data={'query': 'Test Query'}, follow_redirects=True)


    assert '<h1 class="mb-5">Search Movie Ratings</h1>' in response_data
    assert '<p class="mb-3">Search for a movie rating below</p>' in response_data
    assert response.status_code == 200
    assert post.status_code == 200

