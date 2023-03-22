# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
from app import get_single_movie

movie_repository = get_movie_repository() 

def test_get_movie_by_id():
    movie = movie_repository.create_movie("abc", "abd", 5)
    searchedMov = movie_repository.get_movie_by_id(movie.movie_id)
    assert searchedMov is not None
    assert searchedMov.director == movie.director
    assert searchedMov.rating == movie.rating
    assert searchedMov.title == movie.title

    mov = movie_repository.get_movie_by_id(1000000)
    assert mov is None

    movi = movie_repository.create_movie("cat", "dog", 25)
    searchedMo = movie_repository.get_movie_by_id(movi.movie_id)
    assert searchedMo is not None
    assert searchedMo.director == movi.director
    assert searchedMo.rating == movi.rating
    assert searchedMo.title == movi.title