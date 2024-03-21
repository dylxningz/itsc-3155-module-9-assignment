from flask.testing import FlaskClient
<<<<<<< HEAD
import pytest
=======
>>>>>>> origin/main

def test_movies_page(test_app):
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')


    assert '<h1 class="mb-5">All Movies</h1>' in response_data, "Page should have a header 'All Movies'"
    assert 'See our list of movie ratings below' in response_data, "Page should contain the description text"
    assert '<table class="table">' in response_data, "Movies should be listed in a table with class 'table'"
    assert '<th>ID</th>' in response_data, "Table should have an 'ID' column"
    assert '<th>Title</th>' in response_data, "Table should have a 'Title' column"
    assert '<th>Director</th>' in response_data, "Table should have a 'Director' column"
<<<<<<< HEAD
    assert '<th>Rating</th>' in response_data, "Table should have a 'Rating' column"
=======
    assert '<th>Rating</th>' in response_data, "Table should have a 'Rating' column"
>>>>>>> origin/main
