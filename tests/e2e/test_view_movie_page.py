# TODO: Feature 4
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()
movie = movie_repository.create_movie("abc", "abd", 5)

def test_view_movie_page(test_app: FlaskClient):
    response = test_app.get(f'/movies/{movie.movie_id}')
    assert response.status_code == 200
    assert bytes(f'<h1 class="pb-2">Title: {movie.title}</h4>', 'utf-8') in response.data
    assert bytes(f'<h4 class="pb-2">Director: {movie.director}</h4>', 'utf-8') in response.data
    assert bytes(f'<h4 class="pb-2">Rating: {movie.rating}</h4>', 'utf-8') in response.data
    assert bytes(f'<button type="submit" class="btn btn-warning" id="submit-btn">Edit</button>', 'utf-8') in response.data
    assert bytes('<button type="submit" class="btn btn-danger" id="submit-btn">Delete</button>', 'utf-8') in response.data

# https://www.educative.io/answers/how-to-convert-strings-to-bytes-in-python