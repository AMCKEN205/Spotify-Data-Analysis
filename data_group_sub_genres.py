from data_loader import top200s, cur_dir
import sys

genre_group_list = \
    [
        "rock", 
        "rap", 
        "folk", 
        "dance", 
        "hip hop", 
        "grime", 
        "drill", 
        "r&b", 
        "edm", 
        "house", 
        "indie", 
        "country", 
        "electronic",
        "funk",
        "pop"
    ]

for key, top200 in top200s.items():
    # locate the apperance of the given genre grouping strings and replace as required
    i = 0
    while i < len(genre_group_list):
        top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[i]), "artist_top_genre"] = genre_group_list[i]
        i += 1

    # handle some special cases
    top200.loc[top200["artist_top_genre"].str.contains("beatlesque"), "artist_top_genre"] = genre_group_list[0]
    # Artist BROCKHAMPTON is the only general rap artist labelled as boyband. 
    top200.loc[top200["Artist"].str.contains("BROCKHAMPTON"), "artist_top_genre"] = genre_group_list[1]
    top200.loc[top200["artist_top_genre"].str.contains("boy band"), "artist_top_genre"] = genre_group_list[9]

    # save grouped data
    try:
        spotify_data_grouped_save_filepath = "{}\\data\\{} Genres Grouped.csv".format(cur_dir, key)
        top200.to_csv(spotify_data_grouped_save_filepath)
        print("Successfully saved grouped spotify data!")
    except:
        print("Error saving spotify data:")
        print(sys.exc_info()[0])





