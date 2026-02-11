"""
Fetch NSE Index Constituents
----------------------------
Usage:
python fetch_nse_index.py "NIFTY SMALLCAP 250"
"""

import requests
import pandas as pd
import os
import sys

BASE_URL = "https://www.nseindia.com/api/equity-stockIndices"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/",
}

def fetch_index_constituents(index_name):
    session = requests.Session()
    session.headers.update(HEADERS)

    # First hit homepage to get cookies
    session.get("https://www.nseindia.com", timeout=10)

    params = {"index": index_name}
    response = session.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    df = pd.DataFrame(data["data"])

    symbols = df["symbol"].tolist()
    return symbols


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError('Usage: python fetch_nse_index.py "INDEX NAME"')

    index_name = sys.argv[1]
    symbols = fetch_index_constituents(index_name)

    os.makedirs("index_tickers", exist_ok=True)
    filename = f"index_tickers/{index_name.replace(' ', '_')}.txt"

    with open(filename, "w") as f:
        for s in symbols:
            f.write(s + "\n")

    print(f"Saved {len(symbols)} tickers to {filename}")

