class Album:
    def __init__(self, title, release_year, artist_id, album_id):
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
        self.album_id = album_id
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Album({self.title}, {self.release_year}, {self.artist_id})"