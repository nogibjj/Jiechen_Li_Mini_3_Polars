"""
Test goes here

"""

from spotify_main import spotify_song


def test_spotify_main():
    # main_data = "spotify_2023.csv"
    result = spotify_song()
    
    print(result)

    # mean value of the 3rd column
    min_3_column = result.iloc[:, 4].min()
    # print(mean_3_column)
    assert min_3_column == 1.0
    # std value of 3rd column 
    std_3_column = result.iloc[:, 4].std()
    # print(std_3_column)
    assert std_3_column == 0.89


if __name__ == "__main__":
    test_spotify_main()
