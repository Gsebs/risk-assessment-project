import os
from fredapi import Fred
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_fred_data(series_id, start_date='2015-01-01'):
    api_key = os.getenv('FRED_API_KEY')  
    fred = Fred(api_key=api_key)
    data = fred.get_series(series_id, start=start_date)
    return data
