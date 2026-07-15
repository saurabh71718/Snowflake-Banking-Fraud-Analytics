"""
Account Generator
-----------------
Generates bank accounts for Nova Global Bank.
"""

import random

import pandas as pd
from faker import Faker

from config.settings import RAW_DATA_DIR, RANDOM_SEED
from config.constants import (
    ACCOUNT_TYPES,
    ACCOUNT_STATUS,
    ACCOUNT_INTEREST
)

fake = Faker()
random.seed(RANDOM_SEED)
Faker.seed(RANDOM_SEED)


def load_customers():
    """
    Load customer master data.
    """
    return pd.read_csv(RAW_DATA_DIR / "customers.csv")


def generate_iban(country_code):
    """
    Generate a synthetic IBAN.
    """
    random_number = random.randint(
        1000000000000000,
        9999999999999999
    )

    return f"{country_code}99NGB{random_number}"


def generate_interest_rate(account_type):
    """
    Generate interest rate based on account type.
    """
    minimum, maximum = ACCOUNT_INTEREST[account_type]

    return round(random.uniform(minimum, maximum), 2)


def generate_opening_balance(account_type):
    """
    Generate opening balance based on account type.
    """

    if account_type == "Savings":
        return random.randint(500, 20000)

    elif account_type == "Current":
        return random.randint(1000, 50000)

    else:
        return random.randint(20000, 500000)


def generate_current_balance(opening_balance):
    """
    Generate current balance from opening balance.
    """

    multiplier = random.uniform(0.40, 2.20)

    return round(opening_balance * multiplier, 2)


def generate_overdraft(account_type):
    """
    Generate overdraft limit.
    """

    if account_type == "Current":
        return random.randint(500, 10000)

    elif account_type == "Business":
        return random.randint(10000, 100000)

    return 0


def generate_accounts():
    """
    Generate bank accounts for all customers.
    """

    customers = load_customers()

    accounts = []

    account_id = 1

    for _, customer in customers.iterrows():

        number_of_accounts = random.choices(
            [1, 2, 3],
            weights=[70, 25, 5],
            k=1
        )[0]

        for _ in range(number_of_accounts):

            account_type = random.choices(
                ACCOUNT_TYPES,
                weights=[65, 25, 10],
                k=1
            )[0]

            opening_balance = generate_opening_balance(account_type)

            current_balance = generate_current_balance(opening_balance)

            interest_rate = generate_interest_rate(account_type)

            overdraft_limit = generate_overdraft(account_type)

            account = {

                "account_id": f"ACC{account_id:08}",

                "customer_id": customer["customer_id"],

                "branch_id": customer["branch_id"],

                "country": customer["country"],

                # Temporary
                "currency": customer["country"],

                "account_type": account_type,

                "account_status": random.choices(
                    ACCOUNT_STATUS,
                    weights=[92, 6, 2],
                    k=1
                )[0],

                "iban": generate_iban(
                    customer["country"][:2].upper()
                ),

                "opening_balance": opening_balance,

                "current_balance": current_balance,

                "interest_rate": interest_rate,

                "overdraft_limit": overdraft_limit,

                "opened_date": fake.date_between(
                    start_date="-10y",
                    end_date="today"
                )

            }

            accounts.append(account)

            account_id += 1

    df = pd.DataFrame(accounts)

    output_file = RAW_DATA_DIR / "accounts.csv"

    df.to_csv(output_file, index=False)

    print(f"✅ Generated {len(df)} accounts")

    print(f"📁 Saved to {output_file}")

    return df