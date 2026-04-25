import pandas as pd
import json
import os   
from datetime import datetime

RAW_DATA_PATH = "data/raw"
TRANSFORMED_DATA_PATH = "data/processed"

def get_latest_file(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    if not files:
        raise FileNotFoundError("No Raw data files found")
    latest_file = max(files, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
    return os.path.join(folder_path, latest_file)

def transform_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        # print(data)
    records = []

    for coin, values in data.items():
        record = {
            "timestamp": datetime.utcnow(),
            "coin": coin,
            "price_usd": values.get("usd"),
            "market_cap": values.get("usd_market_cap"),
            "volume_24h": values.get("usd_24h_vol"),
            "change_24h": values.get("usd_24h_change")
        }   

        records.append(record)
    # print(records)
    df = pd.DataFrame(records)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df
    
def save_transformed_data(df):
    os.makedirs(TRANSFORMED_DATA_PATH, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    file_path = f"{TRANSFORMED_DATA_PATH}/crypto_transformed_{timestamp}.csv"

    df.to_csv(file_path, index=False)
    print(f"Transformed data saved to {file_path}")

def main():
    latest_file = get_latest_file(RAW_DATA_PATH)
    df = transform_data(latest_file)
    save_transformed_data(df)

if __name__ == "__main__":
    main()


