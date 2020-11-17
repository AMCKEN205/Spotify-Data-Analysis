import matplotlib.pyplot as plot
from data_loader import top200s_grouped


for top200_title,top200 in top200s_grouped.items():
    # Create a new figure instance to ensure we don't try and reuse the same window between plots
    plot_figure = plot.figure()
    plot_params = 111
    
    top200_genres_counts = top200.groupby(["artist_top_genre"]).size().sort_values(ascending=False)

    # Setup genre class bar chart
    top200_xlabels = list(map(str, top200_genres_counts.keys()))
    top200_ylabels = list(top200_genres_counts.values)

    top200_class_ax = plot_figure.add_subplot(plot_params)
    top200_class_ax.barh(top200_xlabels, top200_ylabels)

    for index, genre_count in enumerate(top200_ylabels):
        top200_class_ax.text(genre_count, index , " "+str(genre_count), color="black", va="center", size="smaller", style="italic", fontweight="light")

    # add a title for barchart
    top200_class_ax.set_title("{} genre appearances".format(top200_title))

    plot.show()
