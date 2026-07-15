-- =====================================================
-- 03_load_data.sql
-- Load Data into Snowflake
-- =====================================================

USE DATABASE BANKING_DB;
USE SCHEMA RAW;

---------------------------------------------------------
-- Load Branches
---------------------------------------------------------

COPY INTO RAW.BRANCHES
FROM @BANK_STAGE/branches.csv
FILE_FORMAT = (FORMAT_NAME = CSV_FORMAT);

---------------------------------------------------------
-- Load Customers
---------------------------------------------------------

COPY INTO RAW.CUSTOMERS
FROM @BANK_STAGE/customers.csv
FILE_FORMAT = (FORMAT_NAME = CSV_FORMAT);

---------------------------------------------------------
-- Load Accounts
---------------------------------------------------------

COPY INTO RAW.ACCOUNTS
FROM @BANK_STAGE/accounts.csv
FILE_FORMAT = (FORMAT_NAME = CSV_FORMAT);

---------------------------------------------------------
-- Validation
---------------------------------------------------------

SELECT COUNT(*) AS BRANCHES FROM RAW.BRANCHES;

SELECT COUNT(*) AS CUSTOMERS FROM RAW.CUSTOMERS;

SELECT COUNT(*) AS ACCOUNTS FROM RAW.ACCOUNTS;