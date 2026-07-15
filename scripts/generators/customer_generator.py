"""
Customer Generator
------------------
Generates customer master data for Nova Global Bank.
"""

import random
from datetime import date

import pandas as pd
from faker import Faker

from config.settings import RAW_DATA_DIR, NUM_CUSTOMERS, RANDOM_SEED
from config.constants import (
    CUSTOMER_SEGMENTS,
    CUSTOMER_RISK_PROFILES,
    GENDERS,
    KYC_STATUS,
    OCCUPATIONS
)

# Initialize Faker
fake = Faker()
random.seed(RANDOM_SEED)
Faker.seed(RANDOM_SEED)


def load_branch_data():
    """
    Load branch master data.
    """

    file_path = RAW_DATA_DIR / "branches.csv"

    return pd.read_csv(file_path)


def calculate_age(dob):
    """
    Calculate age from date of birth.
    """

    today = date.today()

    age = (
        today.year
        - dob.year
        - ((today.month, today.day) < (dob.month, dob.day))
    )

    return age


def generate_income(country):
    """
    Generate realistic annual income based on country.
    """

    income_ranges = {
        "United States": (45000, 180000),
        "Canada": (40000, 150000),
        "United Kingdom": (35000, 140000),
        "Germany": (35000, 120000),
        "France": (32000, 110000),
        "Australia": (50000, 170000),
        "Singapore": (50000, 170000),
        "Japan": (4000000, 12000000),
        "United Arab Emirates": (80000, 350000),
        "Switzerland": (70000, 220000),
    }

    minimum, maximum = income_ranges[country]

    return random.randint(minimum, maximum)


def assign_customer_segment(income):
    """
    Assign customer segment based on income.
    """

    if income >= 150000:
        return "Private Banking"

    elif income >= 80000:
        return "Premium"

    else:
        return "Retail"

def generate_customers():
    """
    Generate customer master data.
    """

    branches = load_branch_data()

    customers = []

    for customer_id in range(1, NUM_CUSTOMERS + 1):

        branch = branches.sample(1).iloc[0]

        gender = random.choice(GENDERS)

        if gender == "Male":
            first_name = fake.first_name_male()
        else:
            first_name = fake.first_name_female()

        last_name = fake.last_name()

        dob = fake.date_of_birth(minimum_age=18, maximum_age=80)

        age = calculate_age(dob)

        income = generate_income(branch["country"])

        customer = {

            "customer_id": f"CUS{customer_id:08}",

            "first_name": first_name,

            "last_name": last_name,

            "gender": gender,

            "date_of_birth": dob,

            "age": age,

            "email": fake.email(),

            "phone": fake.phone_number(),

            "country": branch["country"],

            "city": branch["city"],

            "branch_id": branch["branch_id"],

            "occupation": random.choice(OCCUPATIONS),

            "annual_income": income,

            "customer_segment": assign_customer_segment(income),

            "risk_profile": random.choices(
                CUSTOMER_RISK_PROFILES,
                weights=[70, 20, 10],
                k=1
            )[0],

            "kyc_status": random.choices(
                KYC_STATUS,
                weights=[94, 4, 2],
                k=1
            )[0],

            "join_date": fake.date_between(
                start_date="-10y",
                end_date="today"
            )
        }

        customers.append(customer)

    df = pd.DataFrame(customers)

    output_file = RAW_DATA_DIR / "customers.csv"

    df.to_csv(output_file, index=False)

    print(f"✅ Generated {len(df)} customers")

    print(f"📁 Saved to {output_file}")

    return df