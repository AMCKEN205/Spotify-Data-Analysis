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
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[0]), "artist_top_genre"] = genre_group_list[0]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[1]), "artist_top_genre"] = genre_group_list[1]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[2]), "artist_top_genre"] = genre_group_list[2]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[3]), "artist_top_genre"] = genre_group_list[3]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[4]), "artist_top_genre"] = genre_group_list[4]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[5]), "artist_top_genre"] = genre_group_list[5]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[6]), "artist_top_genre"] = genre_group_list[6]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[7]), "artist_top_genre"] = genre_group_list[7]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[8]), "artist_top_genre"] = genre_group_list[8]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[9]), "artist_top_genre"] = genre_group_list[9]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[10]), "artist_top_genre"] = genre_group_list[10]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[11]), "artist_top_genre"] = genre_group_list[11]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[12]), "artist_top_genre"] = genre_group_list[12]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[13]), "artist_top_genre"] = genre_group_list[13]
    top200.loc[top200["artist_top_genre"].str.contains(genre_group_list[14]), "artist_top_genre"] = genre_group_list[14]
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





