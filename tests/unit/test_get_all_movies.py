# TODO: Feature 1

from app import list_all_movies
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_list_all_movies():
    movie=get_movie_repository()
    movie.clear_db
    creed=movie.create_movie("Creed","Micheal B. Jordan",9) #returns a movie
    john_wick=Movie(8,"John Wick","Keanu Reeves", 7)
    target=movie.get_all_movies() #what does this return?
    
    ids_list=[]
    titles_list=[]
    directors_list=[]
    ratings_list=[]
    for key, values in target.items():
        ids_list.append(values.movie_id)
        titles_list.append(values.title)
        directors_list.append(values.director)
        ratings_list.append(values.rating)

    assert "Creed" == titles_list[0]
    assert "Micheal B. Jordan" == directors_list[0]
    assert 9 == ratings_list[0]
    assert "John Wick" not in titles_list
    assert "Keanu Reeves Reeves" not in directors_list
    assert 7 not in ratings_list

    # john_wick=Movie(8,"John Wick","Keanu Reeves", 7)

    # assert creed == target.values()
    # assert john_wick not in movies