import pandas as pd

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import os

import re

# Setup uk song data CSV files 
cur_dir = os.path.dirname(os.path.realpath(__file__))

uk_spotify_data_filepath = "{}\\data\\top_200_gb_data_split".format(cur_dir)
uk_spotify_data_files = os.listdir(uk_spotify_data_filepath)

# Setup spotify api credentials using environment variables 
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

songs_done_count = 0

uk_songs_df = pd.DataFrame()

# Get data from spotify
for spotify_data_filename in uk_spotify_data_files:

    spotify_data = pd.read_csv("{}/{}".format(uk_spotify_data_filepath,spotify_data_filename), skiprows=1)

    for index, row in spotify_data.iterrows():
        # Extract data from spotify API

        song_url = row["URL"]
        song_id = song_url.split("/")[-1]
        
        song_basic_data = spotify.track(song_id)
        song_audio_features = spotify.audio_features(song_id)

        # Double check we're getting the correct artist id before going on to retrieve info based on it
        song_main_artist_basic = song_basic_data.get("artists")[0]
        song_main_artist_id = song_main_artist_basic.get("id")

        song_main_artist = spotify.artist(song_main_artist_id)

        if song_main_artist.get("name") != row["Artist"]:
            print("Error with track {}, artist {} doesn't match artist retrieved from Spotify: {}".format\
                    (
                        row["Track Name"], row["Artist"], song_main_artist
                    )
                )
            break

        # Extract individual attributes for the current song that we'll want to use

        # Attributes already in the original CSV
        artist = row["Artist"]
        position = row["Position"]
        streams = row["Streams"]
        track_name = row["Track Name"]
        week =  re.sub(r"|".join(map(re.escape, ["regional-gb-weekly-", ".csv"])),"",spotify_data_filename)


        # Artist attributes
        try:
            artist_top_genre = song_main_artist.get("genres")[0]
        except:
            artist_top_genre = "Missing"

        # Song basic data attributes
        album = song_basic_data.get("album").get("name")
        release_date = song_basic_data.get("album").get("release_date")
        length = song_basic_data.get("duration_ms")
        popularity = song_basic_data.get("popularity")

        # Song audio feature attributes
        danceability = song_audio_features[0].get("danceability")
        acousticness = song_audio_features[0].get("acousticness")
        energy = song_audio_features[0].get("energy")
        instrumentalness = song_audio_features[0].get("instrumentalness")
        liveness = song_audio_features[0].get("liveness")
        loudness = song_audio_features[0].get("loudness")
        speechiness = song_audio_features[0].get("speechiness")
        tempo = song_audio_features[0].get("tempo")
        time_signature = song_audio_features[0].get("time_signature")

        # Although mixing " " or _ and upper or lower case is odd the original south african data does this, 
        # so do it too for simplicity's sake.
        song_dict = \
            {
                "Artist":artist, 
                "Position":position, 
                "Streams":streams, 
                "Track Name":track_name, 
                "Week":week,
                "album":album,
                "artist_top_genre":artist_top_genre,
                "release_date":release_date,
                "length":length,
                "popularity":popularity,
                "danceability":danceability,
                "acousticness":acousticness,
                "energy":energy,
                "instrumentalness":instrumentalness,
                "liveness":liveness,
                "loudness":loudness,
                "speechiness":speechiness,
                "tempo":tempo,
                "time_signature":time_signature
            }

        uk_songs_df = uk_songs_df.append(song_dict, ignore_index=True)

        songs_done_count += 1
        print("got data for song: {} song no.{}".format(track_name, songs_done_count))

try:
    uk_spotify_data_complete_save_filepath = "{}\\data\\UK_Spotify_data.csv".format(cur_dir)
    uk_songs_df.to_csv(uk_spotify_data_complete_save_filepath)
    print("Successfully retrieved spotify data!")
except:
    print("Error when trying to save spotify data!")
