import pandas as pd
import sqlite3
import os

# Paths
EXCEL_FILE = 'data/active_enterprises - 2026-03-04.xlsx'
DB_FILE = 'data/statistics.db'

def migrate():
    if not os.path.exists(EXCEL_FILE):
        print(f"Error: {EXCEL_FILE} not found.")
        return

    print(f"Reading {EXCEL_FILE}...")
    # Force kved to be a string to avoid numeric conversion issues
    df = pd.read_excel(EXCEL_FILE, dtype={'kved': str})

    # Clean column names (e.g., remove 'year_' prefix if desired, but keeping it for clarity)
    # The columns are already in a good format based on the initial check.

    # Connect to SQLite
    conn = sqlite3.connect(DB_FILE)
    
    print(f"Writing data to {DB_FILE} in table 'active_enterprises'...")
    df.to_sql('active_enterprises', conn, if_exists='replace', index=False)
    
    # Create an index on kved and business_size for faster querying
    conn.execute("CREATE INDEX idx_kved ON active_enterprises (kved)")
    conn.execute("CREATE INDEX idx_business_size ON active_enterprises (business_size)")
    
    conn.close()
    print("Migration completed successfully.")

if __name__ == "__main__":
    migrate()
