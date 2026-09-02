import duckdb
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
DB_PATH = Path(__file__).parent.parent / "warehouse.duckdb"

con = duckdb.connect(str(DB_PATH))
con.execute("CREATE SCHEMA IF NOT EXISTS raw;")

con.execute(f"""
    CREATE OR REPLACE TABLE raw.hcp_master AS
    SELECT * FROM read_csv_auto('{RAW_DIR / "hcp_master.csv"}', header=True)
""")

n = con.execute("SELECT COUNT(*) FROM raw.hcp_master").fetchone()[0]
print(f"Loaded {n} rows into raw.hcp_master")

con.close()