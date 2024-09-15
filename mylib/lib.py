"""
    library file
"""

# Import relevant libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading the data
dataset = "https://storage.googleapis.com/kagglesdsdata/datasets/1807380/9388199/sp500_companies.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240914%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240914T215251Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=3c91ebd790ab9b28b15e5b1be3d8086b8e990455b209d35ea283cd1ab367ca41374bcbd958b7fdec23c62c2915a714733f120df28df968675f985924f47cc1b8a22a7b5272f3a7ee31fd938b008ce905aa2b9241e100f63b2cc8cd816cbe80d89486c7b2cb3944289b634e98acea77aa7c0d799278dc5ba3356c1bf6b2f8396fc9611c3c923b30cedbc0607ac8bcacc92413b41e943ba5c47381611998e7df485f435e5f44a03b7c9af85f014201d4c93ded1917d33accc0359ed44c804e93c56f4e72ef8c8c850819cec6a4ed8b7ad9572ae27bfb333eb6c8ba4543bc29a070b04aecca8440fd1d53993e041c4d7a89f09ab2c3ba986f09b1aa02e20a9a1321"


def load_dataset(dataset):
    """loads the dataset"""
    content_df = pd.read_csv(dataset)
    return content_df


# Data Calculation
def grab_mean(content_df, col):
    """returns the mean of a column"""
    col_mean = content_df[col].mean()
    return col_mean


def grab_median(content_df, col):
    """returns the median of a column"""
    col_median = content_df[col].median()
    return col_median


def grab_std_deviation(content_df, col):
    """returns the standard deviation of a column"""
    col_std_deviation = content_df[col].std()
    return col_std_deviation


def grab_min(content_df, col):
    """returns the minimum value inside a column"""
    col_min = content_df[col].min()
    return col_min


def grab_max(content_df, col):
    """returns the maximum value inside a column"""
    col_max = content_df[col].max()
    return col_max


# Data Visualization: Market Cap Distribution Histogram
def histogram_revenue_growth_distribution(content_df, col_selected):

    plt.figure(figsize=(8, 6))
    plt.hist(content_df.iloc[:, 7], bins=10, edgecolor="black")
    plt.title("Revenue Growth Distribution")
    plt.xlabel("Revenue Growth (%)")
    plt.ylabel("Number of Companies")
    plt.grid(True)
    plt.show()
    # Save the plot if col_selected is not provided, otherwise show it
    if not col_selected:
        plt.savefig("market_cap_distribution.png")
    else:
        plt.show()
