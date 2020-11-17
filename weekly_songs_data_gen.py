from data_loader import UK_top200_grouped, SA_top200_grouped
from statistics import mean
import pandas as pd

# Setup dependencies
genres_to_retrieve = ["pop", "dance", "rap", "hip hop"]

UK_top_200_prevalent_genres = UK_top200_grouped[UK_top200_grouped["artist_top_genre"].isin(genres_to_retrieve)]
SA_top_200_prevalent_genres = SA_top200_grouped[SA_top200_grouped["artist_top_genre"].isin(genres_to_retrieve)]

top_200_split_weeks = list(UK_top_200_prevalent_genres["Week"].unique())

# store the data for songs in each genre using both charts
genre_shared_and_distinct_data_weekly = dict.fromkeys(top_200_split_weeks)

# Group by week so we can retrieve each week for individual analysis
UK_week_dfs_grouped = UK_top_200_prevalent_genres.groupby(UK_top_200_prevalent_genres.Week)
SA_week_dfs_grouped = SA_top_200_prevalent_genres.groupby(SA_top_200_prevalent_genres.Week)

for week in top_200_split_weeks:
    # Generate specified week chart dataframes from UK and SA 
    UK_week_df = UK_week_dfs_grouped.get_group(week)
    SA_week_df = SA_week_dfs_grouped.get_group(week)


    grouped_df = UK_week_df.merge\
        (
            # Merge both dataframes on column values that should be identical
            SA_week_df, 
            on=
                [
                    "Artist",
                    "Track Name",
                    "artist_top_genre",
                    "Week",
                    "acousticness",
                    "album",
                    "danceability",
                    "energy",
                    "instrumentalness",
                    "length",
                    "liveness",
                    "loudness",
                    "speechiness",
                    "tempo",
                    "time_signature"
                ],
            # And distinguish columns that differ in each chart week dataframe
            suffixes=
                [
                    "_UK", 
                    "_SA"
                ],

        )
    
    # Then perform analysis on each genre within the context of an individual week. 
    genres_grouped_df = grouped_df.groupby("artist_top_genre")
    UK_week_df = UK_week_df.groupby("artist_top_genre")
    SA_week_df = SA_week_df.groupby("artist_top_genre")

    genres_weekly_info = dict.fromkeys(genres_to_retrieve)

    for genre in genres_to_retrieve:

        # Get info on shared song counts
        genre_grouped_df = None
        try:
            genre_grouped_df = genres_grouped_df.get_group(genre)
            songs_shared_count = len(genre_grouped_df.index)
        except:
            print("genre: {} has no shared charts songs in week: {}".format(genre, week))
            songs_shared_count = 0
        
        UK_week_genre_df = UK_week_df.get_group(genre)
        SA_week_genre_df = SA_week_df.get_group(genre)

        songs_distinct_count_UK = len(UK_week_genre_df.index) - songs_shared_count 
        songs_distinct_count_SA = len(SA_week_genre_df.index) - songs_shared_count

        # Get info on streams and chart positions in current week's chart

        # Don't perform any 'shared' analysis on streams as UK user base is far larger than SA's, skewing results.
        genre_week_streams_UK = list(UK_week_genre_df.Streams)
        genre_week_streams_SA = list(SA_week_genre_df.Streams)

        genre_week_chart_pos_UK = list(UK_week_genre_df.Position)
        genre_week_chart_pos_SA = list(SA_week_genre_df.Position)

        genre_week_chart_pos_differences = list()
        if genre_grouped_df is None:
            # use null value to not include result in further analysis tasks
            genre_week_chart_pos_differences = None
        else:
            for index,song in genre_grouped_df.iterrows():
                if song["Position_UK"] > song["Position_SA"]:
                    difference = song["Position_UK"] - song["Position_SA"]
                else:
                    difference = song["Position_SA"] - song["Position_UK"]
                genre_week_chart_pos_differences.append(difference)
        

        genres_weekly_info.update\
            (
                {
                    genre : 
                        {
                            "songs_shared_count" : songs_shared_count,
                            "songs_distinct_count_UK" : songs_distinct_count_UK,
                            "songs_distinct_count_SA" : songs_distinct_count_SA,
                            "week_streams_UK" : genre_week_streams_UK,
                            "week_streams_SA" : genre_week_streams_SA,
                            "week_chart_UK" : genre_week_chart_pos_UK,
                            "week_chart_SA" : genre_week_chart_pos_SA,
                            "week_chart_difs" : genre_week_chart_pos_differences
                        } 
                }
            )
        
    genre_shared_and_distinct_data_weekly.update({week : genres_weekly_info})


weekly_song_df = pd.DataFrame.from_dict\
    (
        {
            (week,genre) : genre_shared_and_distinct_data_weekly[week][genre]
            for week in genre_shared_and_distinct_data_weekly.keys()
            for genre in genre_shared_and_distinct_data_weekly[week].keys()
        },
        orient="index" 
    )
print(weekly_song_df.loc["2019-10-11--2019-10-18","pop"])