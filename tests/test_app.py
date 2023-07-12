
"""
When i call POST /albums with album info
That album is now in the lst of GET /albums
"""

"""
When i call GET /albums
I get alist f albums back
"""

def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""\
        "Album(The Cold Nose, 2009, 1)"
    

def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums", data={
        'title': 'In Ear Pork',
        'release_year': '2008',
        'artist_id': '1',
        'album_id': '2'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""
    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(The Cold Nose, 2009, 1)\n" \
        "Album(In Ear Pork, 2008, 1)"
        
def test_post_albums_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "" \
        "You need to submit a title, release_year, and artist_id"
    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(The Cold Nose, 2009, 1)"


#Scenario 1

# POST /albums
# title: "In Ear Pork"
# release_year: 2008
# artist_id: 1
# Expected Response (200 ok)

"""
(no content)
"""

# GET /albums
# title: "In Ear Pork"
# release_year: 2008
# artist_id: 1
# Expected Response (200 ok)

"""
Album(1, The Cold Nose, 2008, 1)
Album(2, In Ear Pork, 2008, 1)
"""


#Scenario 2

# POST /albums
# Expected Response (400 bad request)

"""
You need to submit a title, release_year and artist_id
"""

# GET /albums
# Expected Response (200 ok)

"""
Album(1, The Cold Nose, 2008, 1)
"""


