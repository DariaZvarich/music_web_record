from lib.album import Album


class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        return [
            Album(row["title"], row["release_year"], row["artist_id"], row["album_id"])
            for row in rows
        ]
    
    def create(self, album):
        self._connection.execute(
            "INSERT INTO albums (title, release_year, artist_id, album_id) VALUES (%s, %s, %s, %s)",
            [album.title, album.release_year, album.artist_id, album.album_id]
        )
        return None