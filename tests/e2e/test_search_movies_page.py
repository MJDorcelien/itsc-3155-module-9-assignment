# TODO: Feature 3

from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

# Get a movie repository instance
movie_repository = get_movie_repository()

# Create a new movie instance and store it in the database
movie = movie_repository.create_movie("Titanic", "James Cameron", 9.8)

# Test function for searching movies
def test_search_movies_page(test_app: FlaskClient):
    # Test displaying search form
    response = test_app.get('/movies/search')
    assert response.status_code == 200
    assert b'Search Movie Ratings' in response.data
    assert b'Search for a movie rating below' in response.data
    assert b'Movie Title:' in response.data
    assert b'Enter movie title' in response.data
    assert b'<button type="submit" class="btn btn-primary">Search</button>' in response.data
    
    # Test searching a movie by its title
    response = test_app.get(f'/movies/search?search_title={movie.title}')
    assert response.status_code == 200
    assert bytes(f'<p>{movie.title} has a rating of {movie.rating}</p>', 'utf-8') in response.data
    
    # Test searching a non-existing movie by its title
    search_title = "invalid"
    response = test_app.get(f'/movies/search?search_title={search_title}')
    assert response.status_code == 200
    assert bytes(f'<p class="text-danger">  No movie found with title invalid </p>', 'utf-8') in response.data 

