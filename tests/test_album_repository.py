from lib.album_repository import AlbumRepository
from lib.album import Album


"""
When i call #all
I get all the albums in the albums table
"""

def test_all(db_connection):
    repository = AlbumRepository(db_connection) 
    assert repository.all() == [
        Album(
            title = "The Cold Nose",
            release_year = 2009,
            artist_id = 1,
            album_id = 1
        )
    ]

"""
When i call #create
i create an album in the database
and i can see it back in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    album = Album(
        title="Test title",
        release_year=2000,
        artist_id=1,
        album_id=1,
    )
    repository.create(album)
    assert repository.all() == [
        Album("The Cold Nose", 2009, 1, 1),
        Album("Test title", 2000, 1, 1)
    ]