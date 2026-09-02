import duckdb
con = duckdb.connect("warehouse.duckdb", read_only=True)
print(con.execute("SELECT * FROM main.stg_hcps LIMIT 5").fetchdf())