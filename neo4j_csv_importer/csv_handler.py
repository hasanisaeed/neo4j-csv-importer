import pandas as pd
import os


class CSVHandler:
    def __init__(self, csv_dir):
        self.csv_dir = csv_dir

    def read_csv(self, filename):
        path = os.path.join(self.csv_dir, filename)
        if os.path.exists(path):
            return pd.read_csv(path)
        raise ValueError(f"CSV file {filename} not found.")
