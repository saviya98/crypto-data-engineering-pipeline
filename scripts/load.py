import pandas as pd
from sqlalchemy import create_engine
import os

TRANSFORMED_DATA_PATH = "data/processed"

#PostgreSQL connection
DB_URI = "postgresql+psycopg2://localhost/crypto_db"

def get_latest_file(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    if not files:
        raise FileNotFoundError("No Transformed data files found")
    
    latest_file = max(
        files,
        key=lambda x: os.path.getctime(os.path.join(folder_path, x))
    )

    return os.path.join(folder_path, latest_file)

def load_to_postgres(file_path):
    df = pd.read_csv(file_path) 

    #Ensure column names match SQL table

    df.columns = ['timestamp', 'coin', 'price_usd', 'market_cap', 'volume_24h', 'change_24h']

    engine = create_engine(DB_URI)

    df.to_sql('crypto_prices', engine, if_exists='append', index=False)

    print(f"Loaded {len(df)} records into the database.")

def main():
    latest_file = get_latest_file(TRANSFORMED_DATA_PATH)
    load_to_postgres(latest_file)

if __name__ == "__main__":
    main()