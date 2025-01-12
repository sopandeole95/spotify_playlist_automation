# Spotify ETL Project 🎵

This project extracts, transforms, and loads data from a Spotify playlist using the Spotify Web API.

## Features
- Fetch playlist details (name, description, owner, total tracks).
- Extract song details (name, artist, album, release date, etc.).
- Save the data to a local CSV or an S3 bucket.

## Files
- `spotify_main.py`: The main script for Spotify ETL.
- `credentials.txt`: Stores Spotify client ID and secret (excluded from GitHub for security).
- `playlist_tracks.csv`: Sample output of the ETL process.

## How to Use
1. Set up your Spotify developer account and create an app to get your client ID and secret.
2. Add your credentials to `credentials.txt`:
3. Install dependencies:
pip install spotipy pandas boto3
Alternatively,
pip install -r requirements.txt
4. Run the script:
python spotify_main.py


Requirements:
Python 3.x
Spotipy
Pandas
Boto3 (optional for S3 upload)


Sample Output:
A snippet of the extracted data:

Song Name	Artist	Album	Release Date
Song 1	Artist 1	Album 1	2023-01-01
Song 2	Artist 2	Album 2	2022-05-15
