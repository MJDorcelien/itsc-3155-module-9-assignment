# TODO: Feature 1

from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_get_all_movies(test_app: FlaskClient):

    movie=get_movie_repository()
    movie.clear_db
    movie.create_movie("Creed","Micheal B. Jordan",9)
    Movie(8,"John Wick","Keanu Reeves", 7)

    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert '<p class="mb-3">See our list of movie ratings below</p>' in response_data
    assert '<th>ID #</th>' in response_data
    assert '<td>Creed</td>' in response_data
    assert '<td>John Wick</td>' not in response_data
