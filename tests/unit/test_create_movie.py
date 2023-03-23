# TODO: Feature 2

from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
from app import create_movie



def test_create_movie():
    movie_repository = get_movie_repository() 
    
    movie = movie_repository.create_movie("xyz", "xyz", 4)
    assert movie.title =='xyz'
    assert movie.director == "xyz"
    assert movie.rating == 4

    assert movie is not None

    movie_repository.clear_db()
    