import duckdb
con = duckdb.connect("warehouse.duckdb", read_only=True)
print(con.execute("SELECT * FROM main.stg_hcps LIMIT 5").fetchdf())

import duckdb
con = duckdb.connect("warehouse.duckdb", read_only=True)
print(con.execute("SELECT * FROM main.hcp_engagement ORDER BY total_calls DESC LIMIT 10").fetchdf())