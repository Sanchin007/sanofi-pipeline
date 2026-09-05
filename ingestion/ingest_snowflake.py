import os
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"

conn = snowflake.connector.connect(
    account="absdzbt-vq73477",
    user="SANCHIN007",
    password=os.environ["SNOWFLAKE_PASSWORD"],
    role="ACCOUNTADMIN",
    warehouse="COMPUTE_WH",
    database="SANOFI_PIPELINE",
    schema="RAW",
)

conn.cursor().execute("CREATE SCHEMA IF NOT EXISTS RAW")

for filename, table_name in [
    ("hcp_master.csv", "HCP_MASTER"),
    ("calls.csv", "SALES_CALLS"),
]:
    df = pd.read_csv(RAW_DIR / filename)
    df.columns = [c.upper() for c in df.columns]  # Snowflake likes uppercase by convention
    success, nchunks, nrows, _ = write_pandas(conn, df, table_name, auto_create_table=True)
    print(f"Loaded {nrows} rows into RAW.{table_name}: {success}")

conn.close()