# TODO: Feature 5
from src.repositories.movie_repository import get_movie_repository 
from src.models.movie import Movie
from app import update_movie

movie_repository = get_movie_repository()


def test_update_movie():
    movie_repository.clear_db()
    movie = movie_repository.create_movie("Cocaine Bear", "Elizabeth Banks", 3)
    movie2 = movie_repository.create_movie("Devil Wears Prada", "David Frankel", 4)
    id = movie.movie_id
    id2 = movie2.movie_id

    up_movie = movie_repository.update_movie(id, "Cocaine Bear", "Elizabeth Banks", 2)
    up_movie2 = movie_repository.update_movie(id2, "The Devil Wears Prada", "David Frankel", 5)
    
    assert up_movie.rating == 2
    assert up_movie.title == movie.title
    assert up_movie.director == movie.director

    assert up_movie2.title != "Devil Wears Prada"
    assert up_movie2.director == movie2.director
    assert up_movie2.rating == 5

