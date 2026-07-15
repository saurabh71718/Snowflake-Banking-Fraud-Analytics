"""
Merchant Generator
------------------
Generates merchant master data for Nova Global Bank.
"""

import random

import pandas as pd
from faker import Faker

from config.settings import RAW_DATA_DIR, NUM_MERCHANTS, RANDOM_SEED
from config.constants import (
    MERCHANT_CATEGORIES,
    MERCHANT_RISK
)
from config.countries import COUNTRIES

fake = Faker()
random.seed(RANDOM_SEED)
Faker.seed(RANDOM_SEED)


def random_risk(category):
    """
    Assign merchant risk based on category.
    """

    high_risk = [
        "Travel",
        "Airlines",
        "Luxury",
        "E-Commerce"
    ]

    if category in high_risk:
        return random.choices(
            ["High", "Medium", "Low"],
            weights=[20, 40, 40],
            k=1
        )[0]

    return random.choices(
        ["Low", "Medium", "High"],
        weights=[70, 25, 5],
        k=1
    )[0]


def generate_merchants():

    merchants = []

    for merchant_no in range(1, NUM_MERCHANTS + 1):

        country = random.choice(COUNTRIES)

        city = random.choice(country["cities"])

        category = random.choice(MERCHANT_CATEGORIES)

        merchants.append({

            "merchant_id": f"MER{merchant_no:06}",

            "merchant_name": fake.company(),

            "merchant_category": category,

            "country": country["country"],

            "country_code": country["country_code"],

            "city": city,

            "risk_level": random_risk(category),

            "is_online": random.choice([True, False]),
                        "created_date": fake.date_between(
                start_date="-15y",
                end_date="today"
            ),

            "latitude": round(
                random.uniform(-90, 90), 6
            ),

            "longitude": round(
                random.uniform(-180, 180), 6
            )

        })

    df = pd.DataFrame(merchants)

    output_file = RAW_DATA_DIR / "merchants.csv"

    df.to_csv(output_file, index=False)

    print(f"✅ Generated {len(df)} merchants")

    print(f"📁 Saved to {output_file}")

    return df