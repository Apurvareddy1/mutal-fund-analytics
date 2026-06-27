import pandas as pd
import sqlite3

# Create database
conn = sqlite3.connect("bluestock_mf.db")

# Load cleaned files
nav_df = pd.read_csv("data/processed/cleaned_nav_119551.csv")
txn_df = pd.read_csv("data/processed/cleaned_08_investor_transactions.csv")

# Save to SQLite
nav_df.to_sql("nav_history", conn, if_exists="replace", index=False)
txn_df.to_sql("investor_transactions", conn, if_exists="replace", index=False)

print("Database created successfully!")

conn.close()zzzzzzzzzz