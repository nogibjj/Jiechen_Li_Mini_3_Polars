"""
Test goes here

"""

from main import csvfile


def test_csvfile():
    main_data = "titanic_main_data.csv"
    result = csvfile(main_data)
    
    # mean value of the 1st column
    mean_1_column = result.iloc[:, 0].mean()
    # print(mean_1_column)
    assert mean_1_column == 446
    # min value of 1st column 
    min_1_column = result.iloc[:, 0].min()
    # print(min_1_column)
    assert min_1_column == 1


if __name__ == "__main__":
    test_csvfile()
