from collections import Counter
from data_loader import top200s
import json

def get_unique_genre_words(top_200s):
    for key,top200 in top200s.items():
        genres = list(top200["artist_top_genre"])

        genre_word_count = dict\
            (
                Counter
                    (
                        genre_word for genre in genres 
                            for genre_word in genre.split()
                    )
            )
        
        genres_and_word_counts_sorted = \
            {
                key: word_count for key, word_count in sorted(genre_word_count.items(), key = lambda word_count: word_count[1], reverse=True)
            }
        
        print("Genre unique word appearance counts for {}".format(key))
        print(json.dumps(genres_and_word_counts_sorted, indent=4))

