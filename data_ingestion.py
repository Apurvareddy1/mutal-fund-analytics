import pandas as pd
import os

path = "data/raw"

print("Data Ingestion Started")

for file in os.listdir(path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(path, file))

        print("File:", file)
        print("Shape:", df.shape)
        print("Columns:", df.columns.tolist())
        print(df.head())