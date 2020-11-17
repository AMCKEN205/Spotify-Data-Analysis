from weekly_songs_data_gen import weekly_song_df, genres_to_retrieve, top_200_split_weeks
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from statistics import mean
import numpy as np
from sklearn.metrics import r2_score
import seaborn as sb

# gen graphs

# matching vs differing song names by genre count means piechart
plot_figure = plt.figure()
plot_params = 221

for genre in genres_to_retrieve:
    # get required data
    songs_shared_counts = list()
    songs_distinct_UK_counts = list()
    songs_distinct_SA_counts = list()

    for week in top_200_split_weeks:
        week_genre_data = weekly_song_df.loc[week,genre]

        songs_shared_counts.append(week_genre_data.songs_shared_count)
        songs_distinct_UK_counts.append(week_genre_data.songs_distinct_count_UK)
        songs_distinct_SA_counts.append(week_genre_data.songs_distinct_count_SA)
    
    # generate plots

    means_piechart_ax = plot_figure.add_subplot(plot_params)
    explode = [0.1,0,0]
    means_piechart_values = [mean(songs_shared_counts), mean(songs_distinct_UK_counts), mean(songs_distinct_SA_counts)]
    means_piechart_labels = ["songs shared across charts", "songs distinct to the UK chart", "songs distinct to the SA chart"]

    means_piechart_ax.pie(means_piechart_values, labels=None, autopct='%1.1f%%',
       startangle=90, explode=explode)
    means_piechart_ax.axis('equal')

    plt.legend(loc=3,labels=means_piechart_labels)

    means_piechart_ax.set_title("{} songs average appearance percentage split across weekly charts".format(genre))

    plot_params += 1


plt.show()

plt.clf()

# matching vs differing song names by genre count means piechart

for genre in genres_to_retrieve:

    plot_figure = plt.figure()
    plot_params = 311

    # get required data

    songs_shared_counts = list()
    songs_distinct_UK_counts = list()
    songs_distinct_SA_counts = list()
    week_labels = list()

    for week in top_200_split_weeks:
        week_genre_data = weekly_song_df.loc[week,genre]

        songs_shared_counts.append(int(week_genre_data.songs_shared_count))
        songs_distinct_UK_counts.append(int(week_genre_data.songs_distinct_count_UK))
        songs_distinct_SA_counts.append(int(week_genre_data.songs_distinct_count_SA))
        week_labels.append(week)
    
    # generate plots

    # numeric values required for x ticks, so generate these based on week_labels length then provide a string 
    # representation in each plot
    xticks = range(len(week_labels))


    shared_songs_timeseries_plot = plot_figure.add_subplot(plot_params)

    # perform linear regression to smooth data for trend analysis
    polylinreg = np.poly1d(np.polyfit(xticks, songs_shared_counts, 4))
    r_squared = r2_score(songs_shared_counts,polylinreg(xticks))

    shared_songs_timeseries_plot.plot(xticks, songs_shared_counts, 'o', label="shared songs counts")
    shared_songs_timeseries_plot.plot(xticks, polylinreg(xticks), 'r', label="regression line")
    plt.ylabel("song apperance count")
    plt.xticks(xticks,week_labels, fontsize=8, rotation=90)
    plt.setp(shared_songs_timeseries_plot.get_xticklabels(), visible=False)
    shared_songs_timeseries_plot.set_title("Counts of songs appearing in both week charts, R^2 = {}".format(r_squared))
    shared_songs_timeseries_plot.yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.legend(loc=1)


    plot_params += 1

    distinct_UK_song_timeseries_plot = plot_figure.add_subplot(plot_params, sharex=shared_songs_timeseries_plot)
    
    # perform linear regression to smooth data for trend analysis
    polylinreg = np.poly1d(np.polyfit(xticks, songs_distinct_UK_counts, 4))
    r_squared = r2_score(songs_distinct_UK_counts,polylinreg(xticks))
    
    distinct_UK_song_timeseries_plot.plot(xticks, songs_distinct_UK_counts, 'o', label="distinct UK songs counts")
    distinct_UK_song_timeseries_plot.plot(xticks, polylinreg(xticks), 'r', label="regression line")
    plt.ylabel("song apperance count")
    plt.xticks(xticks,week_labels, fontsize=8, rotation=90)
    plt.setp(distinct_UK_song_timeseries_plot.get_xticklabels(), visible=False)
    distinct_UK_song_timeseries_plot.set_title("Counts of songs appearing only in UK week chart, R^2 = {}".format(r_squared))
    distinct_UK_song_timeseries_plot.yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.legend(loc=1)


    plot_params += 1

    distinct_SA_song_timeseries_plot = plot_figure.add_subplot(plot_params, sharex=shared_songs_timeseries_plot)

    # perform linear regression to smooth data for trend analysis
    polylinreg = np.poly1d(np.polyfit(xticks, songs_distinct_SA_counts, 4))
    r_squared = r2_score(songs_distinct_SA_counts,polylinreg(xticks))

    distinct_SA_song_timeseries_plot.plot(xticks, songs_distinct_SA_counts, 'o', label="distinct SA songs counts")
    distinct_SA_song_timeseries_plot.plot(xticks, polylinreg(xticks), 'r', label="regression line")

    plt.xlabel("chart week")
    plt.ylabel("song apperance count")
    plt.xticks(xticks,week_labels, fontsize=8, rotation=90)
    distinct_SA_song_timeseries_plot.set_title("Counts of songs appearing only in SA week chart, R^2 = {}".format(r_squared))
    distinct_SA_song_timeseries_plot.yaxis.set_major_locator(MaxNLocator(integer=True))
    
    plot_figure.suptitle("{} songs appearance counts as chart weeks timeseries".format(genre))

    plt.legend(loc=1)


    plt.show()

plt.clf()

# Boxplots of stream data

for genre in genres_to_retrieve:
    plot_figure = plt.figure()
    plot_params = 121

    genre_weekly_stats = weekly_song_df.loc[(slice(None), genre), :]
    week_labels = top_200_split_weeks

    # numeric values required for x ticks, so generate these based on week_labels length then provide a string 
    # representation in each plot
    xticks = range(len(week_labels))

    




# Boxplots of chart data
    