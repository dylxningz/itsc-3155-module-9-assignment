from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    movie_repo = get_movie_repository()
    movies_dict = movie_repo.get_all_movies()
    movies_list = list(movies_dict.values())
    return render_template('list_all_movies.html', movies=movies_list, list_movies_active=True)

@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    title = request.form.get('title')
    director = request.form.get('director')
    rating = int(request.form.get('rating'))

    movie_repository.create_movie(title, director, rating)
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')

@app.route('/movies/search', methods=['GET','POST'])
def search_movies():
    # TODO: Feature 3
    if request.method == "POST":
        searched_movie = request.form.get("search")
        movie = movie_repository.get_movie_by_title(searched_movie)
        if movie:
            return redirect(f'/movies/{movie.movie_id}')
        
        
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4

    
  

    movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('get_single_movie.html', movie=movie)




@app.route('/movies/<int:movie_id>/edit', methods=['GET'])
def get_edit_movies_page(movie_id: int):
    movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('edit_movies_form.html', movie=movie)


@app.route('/movies/<int:movie_id>', methods=['POST'])
def update_movie(movie_id: int):
    title = request.form.get('movie_name')
    director = request.form.get('director')
    rating = int(request.form.get('rating'))

    movie_repository.update_movie(movie_id, title, director, rating)

    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    movie_repository.delete_movie(movie_id)
    return redirect('/movies')

