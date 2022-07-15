from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

#######################################  Authorization for Spotify API  #########################################

SPOTIFY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

#Using the Spotipy API Authentication Constructor SpotifyOAuth to authenticate
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

#Getting the user's id
user_id = sp.current_user()["id"]


####################################### Web Scraping and Searching for Songs on Spotify ########################

#Getting User Input for a Date. We then lookup the hot 100 billboard chart of the given date
date = input("Input date in the form YYYY-MM-DD\n")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
response_text = response.text

#Making a 'soup' of the billboard and isolating the song titles in the html from all the other elements
soup = BeautifulSoup(response_text,"html.parser")
class_name = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"
titles = soup.find(name="h3",class_= class_name)
song_names = [name.getText().strip() for name in soup.find_all(name="h3",class_=class_name)]

#Searching the song uri's to add them to a list in order to identify them
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Now we create a new playlist and add the songs to the playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)