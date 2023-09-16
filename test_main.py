"""
Test goes here

"""
import polars as pl
from spotify_main import spotify_song


# Define a test function
def test_top_songs():
    # Read the CSV file
    df = pl.read_csv('spotify_2023.csv', ignore_errors=True)

    # Sort the DataFrame by 'streams' in descending order
    df_sorted = df.sort("streams")

    # Select the top 10 songs
    top_songs = df_sorted.head(10)

    # Assert that the top_songs DataFrame has 10 rows 
    expected_columns = ['track_name', 'streams', 'bpm', 'key', 'mode', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%']
    assert len(top_songs) == 10


# Run the test
if __name__ == "__main__":
    test_top_songs()



# def test_spotify_main():
#     # main_data = "spotify_2023.csv"
#     # result = spotify_song()
    
#     # print(result)

#     # mean value of the 3rd column
#     # min_3_column = result.iloc[:, 4].min()
#     # min_artist_count = result['artist_count'].min()
#     # print(min_3_column)
#     # expected_min_artist_count = 1.0
#     assert min_streams == 2762
#     # std value of 3rd column 
#     # std_3_column = result['artist_count'].std()
#     assert == 5.6686e8


# if __name__ == "__main__":
#     test_spotify_main()
