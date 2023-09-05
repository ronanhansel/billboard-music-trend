import json
import requests
f = open('spotify_secret.json')
sp = json.load(f)
client_id = sp['ID']
client_secret = sp['Key']

def get_token():
    auth_url = "https://accounts.spotify.com/api/token"
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    auth_response = requests.post(auth_url, data=data)
    access_token = auth_response.json().get('access_token')
    return access_token