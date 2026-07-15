-- =====================================================
-- 04_create_views.sql
-- Banking Fraud Analytics
-- =====================================================

USE DATABASE BANKING_DB;
USE SCHEMA ANALYTICS;

---------------------------------------------------------
-- CUSTOMER SUMMARY
---------------------------------------------------------

CREATE OR REPLACE VIEW CUSTOMER_SUMMARY AS

SELECT

    C.CUSTOMER_ID,
    C.FIRST_NAME,
    C.LAST_NAME,
    C.GENDER,
    C.AGE,
    C.COUNTRY,
    C.CITY,
    C.OCCUPATION,
    C.ANNUAL_INCOME,
    C.CUSTOMER_SEGMENT,
    C.RISK_PROFILE,
    C.KYC_STATUS,

    COUNT(A.ACCOUNT_ID) AS TOTAL_ACCOUNTS,

    SUM(A.CURRENT_BALANCE) AS TOTAL_BALANCE,

    AVG(A.CURRENT_BALANCE) AS AVG_BALANCE,

    MAX(A.CURRENT_BALANCE) AS HIGHEST_ACCOUNT_BALANCE

FROM RAW.CUSTOMERS C

LEFT JOIN RAW.ACCOUNTS A
ON C.CUSTOMER_ID = A.CUSTOMER_ID

GROUP BY

    C.CUSTOMER_ID,
    C.FIRST_NAME,
    C.LAST_NAME,
    C.GENDER,
    C.AGE,
    C.COUNTRY,
    C.CITY,
    C.OCCUPATION,
    C.ANNUAL_INCOME,
    C.CUSTOMER_SEGMENT,
    C.RISK_PROFILE,
    C.KYC_STATUS;
