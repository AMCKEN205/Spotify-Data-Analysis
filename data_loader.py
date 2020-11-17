import os
import pandas as pd


cur_dir = os.path.dirname(os.path.realpath(__file__))

# raw top 200s
UK_data_filepath = "{}\\data\\UK_Spotify_data.csv".format(cur_dir)
SA_data_filepath = "{}\\data\\SA_Spotify_data.csv".format(cur_dir)

UK_top200 = pd.read_csv(UK_data_filepath)
SA_top200 = pd.read_csv(SA_data_filepath)
top200s = {"UK Top 200" : UK_top200, "SA Top 200" : SA_top200}

# unique songs
UK_top200_unique = UK_top200.drop_duplicates(subset=["Artist", "Track Name"])
SA_top200_unique = SA_top200.drop_duplicates(subset=["Artist", "Track Name"])
top200s_unique = {"UK Top 200" : UK_top200_unique, "SA Top 200" : SA_top200_unique}

# sub-genres grouped
UK_data_grouped_filepath = "{}\\data\\UK Top 200 Genres Grouped.csv".format(cur_dir)
SA_data_grouped_filepath = "{}\\data\\SA Top 200 Genres Grouped.csv".format(cur_dir)

UK_top200_grouped =pd.read_csv(UK_data_grouped_filepath)
SA_top200_grouped = pd.read_csv(SA_data_grouped_filepath) 

top200s_grouped = {"UK Top 200" : UK_top200_grouped, "SA Top 200" : SA_top200_grouped}