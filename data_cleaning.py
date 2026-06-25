import pandas as pd
import os

raw_path = "data/raw"

for file in os.listdir(raw_path):
    if file.endswith(".csv"):
        print(f"\nProcessing: {file}")

        df = pd.read_csv(os.path.join(raw_path, file))

        print("Rows, Columns:", df.shape)
        print("Missing Values:")
        print(df.isnull().sum())

        df = df.drop_duplicates()

        print("Duplicates Removed")

        output_path = f"data/processed/cleaned_{file}"
        df.to_csv(output_path, index=False)

        print(f"Saved: {output_path}")

print("Data Cleaning Complete")