import os
import sqlite3
import pandas as pd

csv_path = 'data/customer_churn_scored.csv'

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"Could not find {csv_path}. Please run train_model.py first.")

df = pd.read_csv(csv_path)

#connecting database
db_path = 'data/churn_analytics.db'
conn = sqlite3.connect(db_path)

# exporting to SQL table
df.to_sql('customer_churn_scored', conn, if_exists='replace', index=False)

print(f"Success! {len(df)} rows loaded into SQL database '{db_path}' under table 'customer_churn_scored'.")

conn.close()
