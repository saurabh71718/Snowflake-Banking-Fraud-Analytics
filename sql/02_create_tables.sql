-- =====================================================
-- 02_create_tables.sql
-- Project: Snowflake Banking Fraud Analytics
-- =====================================================

USE DATABASE BANKING_DB;
USE SCHEMA RAW;

-- =====================================================
-- BRANCHES
-- =====================================================

CREATE OR REPLACE TABLE RAW.BRANCHES (

    BRANCH_ID STRING,
    BANK_NAME STRING,
    BRANCH_NAME STRING,
    BRANCH_TYPE STRING,

    COUNTRY STRING,
    COUNTRY_CODE STRING,
    CITY STRING,
    REGION STRING,

    CURRENCY STRING,
    TIMEZONE STRING,

    SWIFT_CODE STRING,

    BRANCH_MANAGER STRING,

    OPENING_DATE DATE

);

-- =====================================================
-- CUSTOMERS
-- =====================================================

CREATE OR REPLACE TABLE RAW.CUSTOMERS (

    CUSTOMER_ID STRING,

    FIRST_NAME STRING,
    LAST_NAME STRING,
    GENDER STRING,

    DATE_OF_BIRTH DATE,
    AGE INTEGER,

    EMAIL STRING,
    PHONE STRING,

    COUNTRY STRING,
    CITY STRING,

    BRANCH_ID STRING,

    OCCUPATION STRING,

    ANNUAL_INCOME NUMBER(12,2),

    CUSTOMER_SEGMENT STRING,

    RISK_PROFILE STRING,

    KYC_STATUS STRING,

    JOIN_DATE DATE

);

-- =====================================================
-- ACCOUNTS
-- =====================================================

CREATE OR REPLACE TABLE RAW.ACCOUNTS (

    ACCOUNT_ID STRING,

    CUSTOMER_ID STRING,

    BRANCH_ID STRING,

    COUNTRY STRING,

    CURRENCY STRING,

    ACCOUNT_TYPE STRING,

    ACCOUNT_STATUS STRING,

    IBAN STRING,

    OPENING_BALANCE NUMBER(18,2),

    CURRENT_BALANCE NUMBER(18,2),

    INTEREST_RATE FLOAT,

    OVERDRAFT_LIMIT NUMBER(18,2),

    OPENED_DATE DATE

);

-- =====================================================
-- VERIFY TABLES
-- =====================================================

SHOW TABLES IN SCHEMA RAW;