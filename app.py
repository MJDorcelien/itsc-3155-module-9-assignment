from flask import Flask, redirect, render_template, request, abort

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    movies_list=movie_repository.get_all_movies()
    ids_list=[]
    titles_list=[]
    directors_list=[]
    ratings_list=[]
    for key, values in movies_list.items():
        ids_list.append(values.movie_id)
        titles_list.append(values.title)
        directors_list.append(values.director)
        ratings_list.append(values.rating)
    n=len(ids_list)
    return render_template('list_all_movies.html', list_movies_active=True, ids_list=ids_list,
                           titles_list=titles_list, directors_list=directors_list,
                           ratings_list=ratings_list, n=n)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    movieName = request.form.get("inputMovieName")
    director = request.form.get("inputDirectorName")
    rating = request.form.get("movieRating")
    movie = movie_repository.create_movie(movieName, director, rating)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
   if request.args.get('search_title'):
       # Get the movie title from the form
       title = request.args['search_title']
       # Look up the movie by its title
       movie = movie_repository.get_movie_by_title(title)
       # If the movie was found, display its rating
       if movie:
           return render_template('search_movies.html', search_active=True, movie=movie)
       # If the movie was not found, display an error message
       else:
           return render_template('search_movies.html', search_active=True, error=f"No movie found with title '{title}'")
   # If the form has not been submitted, just display the search form
   return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    movie = movie_repository.get_movie_by_id(movie_id)
    print(movie)
    print(movie_repository.get_all_movies())
    if not movie:
        return abort(404)
    return render_template('get_single_movie.html', movie=movie)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    movie=movie_repository.get_movie_by_id(movie_id)
    return render_template('edit_movies_form.html', movie=movie)


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    newtitle = request.form.get('title')
    newdirector = request.form.get('director')
    newrating = request.form.get('rating')
    id = movie_id
    movie_repository.update_movie(id,newtitle, newdirector, newrating)
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
