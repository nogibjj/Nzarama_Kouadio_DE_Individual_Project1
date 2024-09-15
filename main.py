"""
Main cli or app entry point
"""

from mylib.lib import *


def general_describe(dataset):
    content_df = load_dataset(dataset)
    return content_df.describe()


def custom_describe(dataset, col):
    content_df = load_dataset(dataset)
    descriptive_dict = {
        "name": col,
        "mean": grab_mean(content_df, col),
        "median": grab_median(content_df, col),
        "std": grab_std_deviation(content_df, col),
        "min": grab_min(content_df, col),
        "max": grab_max(content_df, col),
    }
    return descriptive_dict


def histogram_created(content_df, col_selected):
    histogram_revenue_growth_distribution(content_df, col_selected)


def save_to_markdown(dataset):
    """save summary report to markdown"""
    content_df = load_dataset(dataset)
    describe_df = general_describe(dataset)
    markdown_table = describe_df.to_markdown()
    histogram_created(content_df, False)
    # Write the markdown table to a file
    with open("finance.md", "a") as file:
        file.write("Describe:\n")
        file.write(markdown_table)
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz](congress_age.png)\n")


if __name__ == "__main__":
    save_to_markdown(dataset)
