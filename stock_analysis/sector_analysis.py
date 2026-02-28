import pandas as pd
import requests
from nselib import capital_market
import io

def get_pro_sectoral_analysis(trade_date):
    try:
        # 1. Fetch Nifty 500 Mapping
        print("Updating Sector Mappings from NSE...")
        n500_url = "https://archives.nseindia.com/content/indices/ind_nifty500list.csv"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(n500_url, headers=headers)
        
        # FIX: Changed status_status to status_code
        if response.status_code == 200:
            n500_df = pd.read_csv(io.StringIO(response.text))
            n500_map = n500_df[['Symbol', 'Industry']].rename(columns={'Symbol': 'SYMBOL', 'Industry': 'Sector'})
        else:
            return "Failed to fetch Sector list from NSE."

        # 2. Fetch Daily Delivery Data
        print(f"Fetching delivery data for {trade_date}...")
        df = capital_market.bhav_copy_with_delivery(trade_date)
        
        # 3. Clean Columns & Data Types
        df.columns = df.columns.str.strip().str.upper()
        
        # Mapping columns to standard names
        rename_map = {
            'DELIV_PER': 'DELIVERY_PCT', 
            'TURNOVER_LACS': 'TURNOVER',
            'CHANGE': 'PCT_CHANGE' # Some bhavcopies have this
        }
        df = df.rename(columns=rename_map)

        # Force numeric conversion
        cols_to_fix = ['DELIVERY_PCT', 'TURNOVER', 'CLOSE']
        for col in cols_to_fix:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')

        # 4. Merge & Filter
        merged_df = pd.merge(df, n500_map, on='SYMBOL', how='inner')

        # 5. Final Aggregation
        sector_analysis = merged_df.groupby('Sector').agg({
            'DELIVERY_PCT': 'mean',
            'TURNOVER': 'sum',
            'SYMBOL': 'count'
        }).rename(columns={'SYMBOL': 'Stock_Count'})

        return sector_analysis.sort_values(by='DELIVERY_PCT', ascending=False)

    except Exception as e:
        return f"System Error: {e}"

# --- RUN ---
report = get_pro_sectoral_analysis("26-02-2026")

print("\n" + "="*50)
print("   PROFESSIONAL SECTOR-WISE ACCUMULATION DATA")
print("="*50)
print(report)
