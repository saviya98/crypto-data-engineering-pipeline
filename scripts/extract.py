import requests
import json
import os
from datetime import datetime

#API Endpoint
API_URL = "https://api.coingecko.com/api/v3/simple/price"

PARAMS = {
    'ids': 'bitcoin,ethereum',
    'vs_currencies': 'usd',
    'include_market_cap': 'true',
    'include_24hr_vol': 'true',
    'include_24hr_change': 'true'
}

def fetch_crypto_data():
    try:
        response = requests.get(API_URL, params=PARAMS, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
def save_raw_data(data):
    if data is None:
        print("No data to save.")
        return
    # Creating folder if it doesn't exist
    os.makedirs('data/raw', exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"data/raw/crypto_{timestamp}.json"

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

        print(f"Raw data saved to {file_path}")

def main():
    data = fetch_crypto_data()
    save_raw_data(data)

if __name__ == "__main__":
    main()