# TODO: Feature 2
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_create_movies_page(test_app: FlaskClient): 
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    response = test_app.get('/movies/new')
    data = response.data.decode('utf-8')
    assert '<div class="form-group">' in data
    assert '<button type="submit" class="btn btn-primary">Submit</button>' in data

    assert '<label for="inputMovieName">Movie Name</label>' in data 
    assert '<input type="name" class="form-control" name="inputMovieName" aria-describedby="movieNameHelp" placeholder="Enter Movie Name">' in data
    
    assert '<label for="inputDirectorName">Director Name</label>' in data 
    assert '<input type="name" class="form-control" name="inputDirectorName" aria-describedby="directorNameHelp" placeholder="Enter Director Name">' in data
   
    assert '<label for="movieRating">Movie Rating</label>' in data 
    
    assert '<select class="form-control" name="movieRating">' in data

    response = test_app.post('/movies', data = {
        "inputMovieName": "Star Wars",
        "inputDirectorName": "J.J. Abrams",
        "movieRating": 4, 
        }, follow_redirects=True) 
    assert response.status_code == 200

    movies = movie_repository.get_all_movies()
    movie = movie_repository.get_movie_by_title("Star Wars")

    assert movies[movie.movie_id].title == "Star Wars"
    assert movies[movie.movie_id].title != "wqaxswe"

    assert movies[movie.movie_id].director == "J.J. Abrams"
    assert movies[movie.movie_id].director != "jkwenolwe"

    assert movies[movie.movie_id].rating == '4'

