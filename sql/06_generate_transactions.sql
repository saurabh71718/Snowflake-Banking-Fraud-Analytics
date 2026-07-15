-- =====================================================
-- 06_generate_transactions.sql
-- Generate Synthetic Transactions
-- =====================================================

USE DATABASE BANKING_DB;
USE SCHEMA RAW;

INSERT INTO RAW.TRANSACTIONS

SELECT

'TXN' || LPAD(SEQ4()+1,10,'0')                AS TRANSACTION_ID,

A.ACCOUNT_ID,

A.CUSTOMER_ID,

A.BRANCH_ID,

DATEADD(

SECOND,

UNIFORM(0,63072000,RANDOM()),

DATEADD(YEAR,-2,CURRENT_TIMESTAMP())

)                                             AS TRANSACTION_TIMESTAMP,

CASE

WHEN UNIFORM(1,100,RANDOM())<=45 THEN 'POS Purchase'

WHEN UNIFORM(1,100,RANDOM())<=65 THEN 'Online Purchase'

WHEN UNIFORM(1,100,RANDOM())<=75 THEN 'ATM Withdrawal'

WHEN UNIFORM(1,100,RANDOM())<=90 THEN 'Bank Transfer'

WHEN UNIFORM(1,100,RANDOM())<=95 THEN 'Salary Credit'

ELSE 'Bill Payment'

END                                           AS TRANSACTION_TYPE,

CASE

WHEN UNIFORM(1,100,RANDOM())<=40 THEN 'Mobile Banking'

WHEN UNIFORM(1,100,RANDOM())<=70 THEN 'POS'

WHEN UNIFORM(1,100,RANDOM())<=85 THEN 'ATM'

ELSE 'Internet Banking'

END                                           AS TRANSACTION_CHANNEL,

CASE

WHEN UNIFORM(1,100,RANDOM())<=97 THEN 'SUCCESS'

WHEN UNIFORM(1,100,RANDOM())<=99 THEN 'FAILED'

ELSE 'REVERSED'

END                                           AS TRANSACTION_STATUS,

A.CURRENCY,

ROUND(

UNIFORM(5,5000,RANDOM())

,2

)                                             AS AMOUNT

FROM

(

SELECT *

FROM RAW.ACCOUNTS

QUALIFY ROW_NUMBER()

OVER(

ORDER BY RANDOM()

)<=13500

) A,

TABLE(GENERATOR(ROWCOUNT=>250000));