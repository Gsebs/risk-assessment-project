from src.data_collection import get_fred_data

# Get GDP data from FRED
gdp_data = get_fred_data('GDP')
print(gdp_data.head())
