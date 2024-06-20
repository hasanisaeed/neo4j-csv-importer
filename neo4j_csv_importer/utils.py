import os


def get_csv_files(directory):
    """Get a list of CSV files in the given directory."""
    return [f for f in os.listdir(directory) if f.endswith('.csv')]
