import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist 
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/albums', methods=['POST'])
def post_album():
    if has_invalid_album_parameters(request.form):
        
        return "You need to submit a title, release_year, and artist_id", 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        title=request.form['title'],
        release_year=request.form['release_year'],
        artist_id=request.form['artist_id'],
        album_id=request.form['album_id']
    )
    repository.create(album)
    return "", 200

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return "\n".join(
        f"{album}" for album in repository.all()
    )
    
def has_invalid_album_parameters(form):
    return 'title' not in form or \
        'release_year' not in form \
        or 'artist_id' not in form
        
        
@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return ", ".join(str(artist) for artist in artists)

@app.route('/artists', methods=['POST'])
def post_artist():
    name = request.form.get('name')
    genre = request.form.get('genre')
    
    if not name or not genre:
        return "You need to submit a name and genre", 400
    
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(name=name, genre=genre)
    repository.create(artist)
    
    return "", 200


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

