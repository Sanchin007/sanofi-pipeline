import duckdb
import pandas as pd

hcps = [
    {"name": "Dr. Martin",  "region": "Paris",     "specialty": "Cardiology"},
    {"name": "Dr. Dubois",  "region": "Lyon",       "specialty": "Endocrinology"},
    {"name": "Dr. Laurent", "region": "Paris",      "specialty": "Cardiology"},
    {"name": "Dr. Bernard", "region": "Marseille",  "specialty": "Immunology"},
    {"name": "Dr. Petit",   "region": "Paris",      "specialty": "Endocrinology"},
]

hcps_df = pd.DataFrame(hcps)
con = duckdb.connect()
con.execute("CREATE TABLE hcps AS SELECT * FROM hcps_df")

# query 1 - HCPs in Lyon or Marseille
print("--- Lyon or Marseille ---")
print(con.execute("""
    SELECT name, region
    FROM hcps
    WHERE region = 'Lyon' OR region = 'Marseille'
""").fetchdf())

# query 2 - count of HCPs per specialty
print("\n--- Count per specialty ---")
print(con.execute("""
    SELECT specialty, COUNT(*) AS hcp_count
    FROM hcps
    GROUP BY specialty
    ORDER BY hcp_count DESC
""").fetchdf())