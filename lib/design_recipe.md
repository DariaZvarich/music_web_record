{{ NAME }} Route Design Recipe
Copy this design recipe template to test-drive a plain-text Flask route.

1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

POST /albums
    title: string
    release_year: number(str)
    artist_id: number(str)





# Home route
GET /home

# Waving route
GET /wave?name=<string>

# Submit message route
POST /submit
  name: string
  message: string
2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

Scenario 1

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


Scenario 2

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






# EXAMPLE

# GET /home
#  Expected response (200 OK):
"""
This is my home page!
"""

# GET /wave?name=Leo
#  Expected response (200 OK):
"""
I am waving at Leo
"""

# GET /wave
#  Expected response (200 OK):
"""
I am waving at no one!
"""

# POST /submit
#  Parameters:
#    name: Leo
#    message: Hello world
#  Expected response (200 OK):
"""
Thanks Leo, you sent this message: "Hello world"
"""

# POST /submit
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a name and a message
"""
3. Test-drive the Route
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
How