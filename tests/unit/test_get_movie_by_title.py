# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_get_movie_by_title():
    # Create a new movie
    movie = movie_repository.create_movie("The Martian", "Ridley Scott", 3.5)

    # Test retrieving the movie by title
    searched_movie = movie_repository.get_movie_by_title("The Martian")
    assert searched_movie is not None
    assert searched_movie.movie_id == movie.movie_id
    assert searched_movie.title == movie.title
    assert searched_movie.director == movie.director
    assert searched_movie.rating == movie.rating

    # Test retrieving a non-existent movie
    searched_movie = movie_repository.get_movie_by_title("Invalid Title")
    assert searched_movie is None