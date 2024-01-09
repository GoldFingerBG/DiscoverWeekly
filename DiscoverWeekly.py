import spotipy
from flask import Flask, redirect, request, url_for
from spotipy.oauth2 import SpotifyOAuth

app = Flask("__name__")

app.secret_key = '7sad6f98as6fas09d8f'
app.config['SESSION_COOKIE_NAME'] = 'My Cookie'
TOKEN_INFO = 'token_info'

@app.route('/')
def home():
    return 'ur mom'

@app.route('/redirect')
def redirect():
    return 'Youve been redirected'

@app.route('/saveDiscoverWeekly')
def project():
    return 'the code'
    #this will be the code for the project

def create_spotify_oauth():
    return SpotifyOAuth(client_id = '3b226c9733d74dac998c8dc0d6a5e129', 
                        client_secret = 'a768935766104030919e5f71863127ce', 
                        redirect_uri = url_for("redirect"), _external = True,
                        scope = 'user-library-read user-library-modify playlist-modify-public playlist-modify-private')

if __name__ == '__main__':
    app.run()