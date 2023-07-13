def test_post_artist(web_client):
    post_data = {
        'name': 'Wild nothing',
        'genre': 'Indie'
    }
    post_response = web_client.post('/artists', data=post_data)
    assert post_response.status_code == 200 or post_response.status_code == 204

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    expected_artists = "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"
    assert response.data.decode('utf-8') == expected_artists