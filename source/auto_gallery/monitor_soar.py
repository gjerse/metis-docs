"""
SOAR Data Flow Monitoring using TAP
===================================

This example demonstrates how to use the **IVOA Table Access Protocol (TAP)** and the `astroquery` library to monitor the count of new data items 
(data products) for Metis and other Solar Orbiter instruments recently 
ingested into the SOAR archive.

The script queries SOAR's metadata tables using ADQL (Astronomy Data Query Language) 
and outputs the results in a readable Markdown table format.

This method is useful for quickly tracking data availability across different 
processing levels (L0, L1, L2, L3, LL).
"""
#%%
# 1. Setup and Parameter Definition
# ---------------------------------
# Import necessary libraries and define constants for the TAP query.
from astroquery.utils.tap.core import TapPlus
from datetime import datetime, timedelta
import pandas as pd
import time
import sys

# Global Configuration
SOAR_URL = 'http://soar.esac.esa.int/soar-sl-tap/tap'
INSTRUMENT_LIST = ['EPD', 'EUI', 'MAG', 'METIS', 'PHI', 'RPW', 'SOLOHI', 'STIX'] 
LEVEL_LIST = ['L1', 'L2', 'L3', 'LL1', 'LL2'] # Focusing on useful levels
DATA_TABLES = {'SC': 'v_sc_data_item', 'LL': 'v_ll_data_item'}

# Define the search period (e.g., the last 7 days)
DAYS_TO_SUBTRACT = 7 
START_DATETIME = datetime.today() - timedelta(days=DAYS_TO_SUBTRACT)
START_TIME_ISO = START_DATETIME.strftime('%Y-%m-%dT%H:%M:%S')

print(f"--- Monitoring SOAR Data Flow ---")
print(f"Searching for new data inserted since: {START_TIME_ISO}")

#%%
# 2. TAP Query Execution Function
# -------------------------------
# This function handles the connection to the TAP service and executes the ADQL query.
# It uses TapPlus.launch_job() for robust, potentially long-running queries.

def execute_query(query, src_str):
    """Executes the ADQL query using TapPlus."""
    try:
        SOAR = TapPlus(url=src_str)
        # Use launch_job for stable execution
        results = SOAR.launch_job(query)
        table = results.get_results()
        return table
    except Exception as e:
        # Print error message to stderr if query fails
        print(f"  [TAP Error] Failed query execution: {e}", file=sys.stderr)
        return None

#%%
# 3. Report Generation and Output
# -------------------------------
# We iterate through instruments and levels, query the item count, and collect results.

report_data = []

for instru in INSTRUMENT_LIST:
    for level in LEVEL_LIST:
        # Determine the correct table (SC or LL)
        table_type = 'LL' if 'LL' in level else 'SC'
        table_name = DATA_TABLES[table_type]

        # Construct the ADQL query string
        ADQL = (
            f"SELECT COUNT(data_item_id) "
            f"FROM {table_name} "
            f"WHERE instrument='{instru}' "
            f"AND level='{level}' "
            f"AND insertion_time>'{START_TIME_ISO}'"
        )

        result_table = execute_query(ADQL, SOAR_URL)
        
        if result_table is not None:
            count = result_table['COUNT'][0]
            
            # Record results only if new data is found
            if count > 0:
                report_data.append({
                    'Instrument': instru,
                    'Level': level,
                    'Count': count
                })
        
        # Short pause (0.5s) to avoid overloading the TAP service
        time.sleep(0.5)

# Convert the collected data into a Pandas DataFrame for final presentation
report_df = pd.DataFrame(report_data)

print("\n--- Summary of New Data Items Found ---")

if not report_df.empty:
    # Sort results and print them as a readable Markdown table
    report_df = report_df.sort_values(by=['Instrument', 'Level'])
    print(report_df.to_markdown(index=False))
else:
    print("No new data items found in the specified interval.")