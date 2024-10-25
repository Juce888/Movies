from flask import Flask, render_template, request

from model.MovieBackend import Movie

app = Flask(__name__)

movie_dictionary = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movie_entry')
def movie_entry():
    return render_template('movie_entry.html')


@app.route('/movie_info', methods=['POST'])
def movie_info():
    movie_title = request.form['movie_title']
    movie_genre = request.form['genre']
    movie_director = request.form['director']
    movie_year = request.form['release_year']

    if movie_title != "":
        movie_dictionary.append({"Title": movie_title, "Genre": movie_genre,
                                 "Director": movie_director, "Year": movie_year})

        return render_template("movie_display.html", Movie=movie_dictionary)
    else:
        return "Movie Title cannot be empty!"


if __name__ == '__main__':
    app.run(debug=True)
