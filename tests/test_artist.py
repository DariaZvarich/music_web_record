from lib.artist import Artist

def test_get_artists(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    expected_artists = "Pixies, ABBA, Taylor Swift, Nina Simone"
    assert response.data.decode('utf-8') == expected_artists
    
    
def test_constructs():
    album = Artist(
        name ="Test Title",
        release_year=2000,
        artist_id=1,
        album_id=1
    )
    assert album.title == "Test Title"
    assert album.release_year == 2000
    assert album.artist_id == 1
    assert album.album_id == 1
    
    
"""
Albums with equal contents are equal
"""

def test_compares():
    album_1 = Album(1, "Test Title", 1000, 2)
    album_2 = Album(1, "Test Title", 1000, 2)
    assert album_1 == album_2
    
"""
Albums can be represented as string
"""

def test_stringifying():
    album = Album(
        title="Test Title",
        release_year=2000,
        artist_id=1,
        album_id=1
    )
    assert str(album) == "Album(Test Title, 2000, 1)"
    
