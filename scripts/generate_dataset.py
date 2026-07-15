"""
Main Dataset Generator
"""

from generators.branch_generator import generate_branches
from generators.customer_generator import generate_customers
from generators.account_generator import generate_accounts
from generators.merchant_generator import generate_merchants

def main():

    print("=" * 60)
    print("🌍 Nova Global Bank Dataset Generator")
    print("=" * 60)

    generate_branches()

    generate_customers()

    generate_accounts()

    print("\n✅ Dataset generation completed.")


if __name__ == "__main__":
    main()