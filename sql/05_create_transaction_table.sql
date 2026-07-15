-- =====================================================
-- 05_create_transaction_table.sql
-- Project : Snowflake Banking Fraud Analytics
-- =====================================================

USE DATABASE BANKING_DB;
USE SCHEMA RAW;

CREATE OR REPLACE TABLE RAW.TRANSACTIONS (

    TRANSACTION_ID          STRING,

    ACCOUNT_ID              STRING,

    CUSTOMER_ID             STRING,

    BRANCH_ID               STRING,

    TRANSACTION_TIMESTAMP   TIMESTAMP,

    TRANSACTION_TYPE        STRING,

    TRANSACTION_CHANNEL     STRING,

    TRANSACTION_STATUS      STRING,

    CURRENCY                STRING,

    AMOUNT                  NUMBER(18,2)

);