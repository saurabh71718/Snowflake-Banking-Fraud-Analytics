"""
Branch Generator
----------------
Generates branch master data for Nova Global Bank.
"""

import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker

from config.settings import RAW_DATA_DIR, NUM_BRANCHES, RANDOM_SEED
from config.constants import BANK_NAME, BRANCH_TYPES
from config.countries import COUNTRIES

fake = Faker()
random.seed(RANDOM_SEED)
Faker.seed(RANDOM_SEED)


def random_opening_date():
    """Return a random branch opening date within the last 25 years."""
    start_date = datetime(2000, 1, 1)
    end_date = datetime.today()

    delta = end_date - start_date

    return (
        start_date + timedelta(days=random.randint(0, delta.days))
    ).date()


def generate_swift(country_code):
    """
    Generate a demo SWIFT/BIC code.

    NOTE:
    These are synthetic values for learning purposes.
    """
    return f"NGBL{country_code}XX"


def generate_branches():

    branches = []

    for branch_id in range(1, NUM_BRANCHES + 1):

        country = random.choice(COUNTRIES)

        city = random.choice(country["cities"])

        branches.append({

            "branch_id": f"BR{branch_id:06}",

            "bank_name": BANK_NAME,

            "branch_name": f"{city} Branch",

            "branch_type": random.choice(BRANCH_TYPES),

            "country": country["country"],

            "country_code": country["country_code"],

            "city": city,

            "region": country["region"],

            "currency": country["currency"],

            "timezone": country["timezone"],

            "swift_code": generate_swift(country["country_code"]),

            "branch_manager": fake.name(),

            "opening_date": random_opening_date()

        })

    df = pd.DataFrame(branches)

    output_file = RAW_DATA_DIR / "branches.csv"

    df.to_csv(output_file, index=False)

    print(f"✅ Generated {len(df)} branches")

    print(f"📁 Saved to {output_file}")

    return df