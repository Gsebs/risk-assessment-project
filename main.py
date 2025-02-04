import os
import sys

# Ensure the project root directory is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_collection import get_fred_data

# Get GDP data from FRED
gdp_data = get_fred_data('GDP')
print(gdp_data.head())

