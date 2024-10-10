from flask import Flask, render_template, request

from model.MovieBackend import Movie

app = Flask(__name__)

new_movies = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movie_entry')
def movie_entry():
    return render_template('movie_entry.html')


@app.route('/movie_info', methods=['POST'])
def movie_info():
    movie_name = request.form['movie_name']
    movie_genre = request.form['genre']
    movie_director = request.form['director']
    movie_year = request.form['release_year']

    if movie_name != '':
        new_movie = Movie(movie_name, movie_genre, movie_director, movie_year)

        new_movies.append({"Title": new_movie.title, "Genre": new_movie.genre,
                           "Director": new_movie.director, "Year": new_movie.year})

        return render_template("moviedisplay.html", items=new_movies)
    else:
        return "Movie Title Cannot be Null."


if __name__ == '__main__':
    app.run(debug=True)
