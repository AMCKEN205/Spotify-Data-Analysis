from numpy.lib.arraysetops import unique
from data_loader import top200s_unique, top200s_grouped
import json

def count_unique_genres(top200s):
    for key, top200 in top200s.items():
        genres = list(unique(top200["artist_top_genre"]))
        genre_counts = list()
        
        for genre in genres:
            genre_counts.append(list(top200["artist_top_genre"]).count(genre))
        
        genres_and_counts = dict(zip(genres, genre_counts))
        genres_and_counts_sorted = \
            {
                key: genre for key, genre in sorted(genres_and_counts.items(), key = lambda genre: genre[1], reverse=True)
            }

        print\
            (
            """
Unique genres in {}: {} genres

Unique genre counts: {}
            """.format(key, len(genres), json.dumps(genres_and_counts_sorted, indent=4))
            )
        print("\n---------------------------------------\n")

#count_unique_genres(top200s_unique)
count_unique_genres(top200s_grouped)