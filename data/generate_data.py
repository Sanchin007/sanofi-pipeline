import random
from pathlib import Path
from tracemalloc import start
import pandas as pd
from faker import Faker

fake = Faker("fr_FR")
random.seed(42)
Faker.seed(42)

RAW_DIR = Path(__file__).parent / "raw"
RAW_DIR.mkdir(exist_ok=True)

SPECIALTIES = ["General Practice", "Cardiology", "Endocrinology", "Immunology"]
REGIONS = ["Paris", "Lyon", "Marseille"]

hcps = []
for i in range(20):
    hcps.append({
        "hcp_id": f"HCP{i:03d}",
        "hcp_name": fake.name(),
        "specialty": random.choice(SPECIALTIES),
        "region": random.choice(REGIONS),
    })

hcp_df = pd.DataFrame(hcps)
hcp_df.to_csv(RAW_DIR / "hcp_master.csv", index=False)

print(f"Generated {len(hcp_df)} HCPs -> {RAW_DIR / 'hcp_master.csv'}")
print(hcp_df.head())




import random 
from datetime import datetime, timedelta

CHANNELS = ["Field Visit", "Virtual call", "Email Detailing"]
start = datetime(2026, 1, 1)

calls = []
for i in range(200):
    call_date = start + timedelta(days=random.randint(0, 240))
    hcp = random.choice(hcps)
    calls.append({
        "call_id": f"CALL{i:04d}",
        "hcp_id": hcp["hcp_id"],
        "call_date": call_date.date().isoformat(),
        "channel": random.choice(CHANNELS),
    })
CALLS_df = pd.DataFrame(calls)
CALLS_df.to_csv(RAW_DIR / "calls.csv", index=False)
print(f"Generated {len(CALLS_df)} calls -> {RAW_DIR / 'calls.csv'}")
print(CALLS_df.head())