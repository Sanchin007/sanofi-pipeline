import random
from pathlib import Path
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