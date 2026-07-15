"""
Project Constants
-----------------
Static values used across the application.
"""

BANK_NAME = "Nova Global Bank"

BRANCH_TYPES = [
    "Retail",
    "Corporate",
    "Digital"
]

ACCOUNT_TYPES = [
    "Savings",
    "Current",
    "Business"
]

CARD_NETWORKS = [
    "Visa",
    "Mastercard",
    "American Express"
]

CARD_TYPES = [
    "Debit",
    "Credit"
]

CUSTOMER_RISK_PROFILES = [
    "Low",
    "Medium",
    "High"
]
CUSTOMER_SEGMENTS = [
    "Retail",
    "Premium",
    "Private Banking"
]

KYC_STATUS = [
    "Verified",
    "Pending",
    "Under Review"
]

GENDERS = [
    "Male",
    "Female"
]

OCCUPATIONS = [
    "Software Engineer",
    "Data Analyst",
    "Teacher",
    "Doctor",
    "Lawyer",
    "Financial Analyst",
    "Business Consultant",
    "Project Manager",
    "Marketing Manager",
    "Sales Executive",
    "Accountant",
    "Research Scientist",
    "Nurse",
    "Student",
    "Entrepreneur"
]
ACCOUNT_STATUS = [
    "Active",
    "Dormant",
    "Closed"
]

ACCOUNT_INTEREST = {
    "Savings": (2.0, 5.0),
    "Current": (0.0, 0.5),
    "Business": (0.5, 2.0)
}

CARD_STATUS = [
    "Active",
    "Blocked",
    "Expired"
]

CARD_LIMITS = {
    "Debit": 0,
    "Credit": [
        1000,
        2500,
        5000,
        10000,
        25000,
        50000
    ]
}
MERCHANT_CATEGORIES = [
    "Grocery",
    "Restaurant",
    "Fuel",
    "Healthcare",
    "Pharmacy",
    "Electronics",
    "Travel",
    "Airlines",
    "Hotels",
    "Fashion",
    "Luxury",
    "Entertainment",
    "Utilities",
    "Education",
    "Insurance",
    "Investment",
    "Telecom",
    "E-Commerce"
]

MERCHANT_RISK = [
    "Low",
    "Medium",
    "High"
]