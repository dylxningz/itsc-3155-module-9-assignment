from flask.testing import FlaskClient

def test_delete_movie_page(test_app: FlaskClient):

    response = test_app.delete('/movies/1/delete')

    assert response.status_code == 200

    response_data = response.data.decode('utf-8')
    assert 'Movie deleted successfully.' in response_data
