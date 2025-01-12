import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd


def run_spotify_etl():
    # with open("credentials.txt") as file:
    #     client_id=file.readline().strip()
    #     client_secret=file.readline().strip()
    
    client_id = "xxxxxxxxxxxxxxxxxxxxxxxx"
    client_secret = "yyyyyyyyyyyyyyyyyyyyyyy"

    # print(client_id)
    print()
    # print(client_secret)    

    redirect_uri = "http://example.com"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                client_secret=client_secret,
                                                redirect_uri=redirect_uri,
                                                scope="playlist-read-private"))

    # Playlist ID (extracted from the URL)
    playlist_id = "zzzzzzzzzzzzzzzzzzzzzzzz"  # Extracted from your provided URL

    # Fetch playlist details
    playlist = sp.playlist(playlist_id)

    # Extract playlist metadata
    playlist_data = {
        "playlist_name": playlist["name"],
        "description": playlist["description"],
        "owner": playlist["owner"]["display_name"],
        "total_tracks": playlist["tracks"]["total"]
    }

    print("Playlist Data:")
    print(playlist_data)

    # Fetch tracks in the playlist
    tracks = playlist["tracks"]
    song_data = []

    # Iterate through tracks and extract song and artist data
    while tracks:
        for item in tracks["items"]:
            track = item["track"]
            artist = track["artists"][0]  # Get the first artist
            
            # Append track and artist details to the song_data list
            song_data.append({
                "song_name": track["name"],
                "song_id": track["id"],
                "duration_ms": track["duration_ms"],
                "popularity": track["popularity"],
                "artist_name": artist["name"],
                "artist_id": artist["id"],
                "album_name": track["album"]["name"],
                "release_date": track["album"]["release_date"]
            })
        
        # Get the next set of tracks if available
        tracks = sp.next(tracks) if tracks["next"] else None

    # Create a DataFrame for the extracted song data
    df = pd.DataFrame(song_data)

    # Print the first few rows of the DataFrame
    print("\nSong and Artist Data:")
    print(df.head())

    # Save the data to a CSV file (optional)
    df.to_csv("playlist_tracks.csv", index=False)
    df.to_csv("s3://sopan-spotify-bucket/playlist_tracks.csv")