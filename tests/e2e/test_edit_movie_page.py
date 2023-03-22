# TODO: Feature 5
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repository = get_movie_repository();
movie_repository.clear_db()
movie = movie_repository.create_movie("Midsommar", "Ari Aster", 9)

def test_edit_movie(test_app: FlaskClient):  
    response = test_app.get(f'/movies/{movie.movie_id}/edit')
    assert response.status_code == 200
    
    assert b'<h2 class="mb-3">Edit movie information below:</h2>' in response.data
    assert b'<label for="title">Title:</label>' in response.data

    response2 = test_app.post(f'/movies/{movie.movie_id}', data={
        'title' : 'Midsommar',
        'director' : 'Ari Aster',
        'rating' : 5 ,
    }, follow_redirects=True)

    assert response2.status_code == 200
    data = response2.data.decode('utf-8')

    assert '<h1 class="pb-2">Title: Midsommar</h4>' in data
    assert '<h4 class="pb-2">Director: Ari Aster</h4>' in data
    assert '<h4 class="pb-2">Rating: 5</h4>' in data

    







