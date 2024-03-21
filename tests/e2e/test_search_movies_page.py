# TODO: Feature 3
from flask.testing import FlaskClient



def test_search_page(test_app):
    response = test_app.get('/movies/search')  
    assert response.status_code == 200