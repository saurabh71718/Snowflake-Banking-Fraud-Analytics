# Solution Architecture

```text
                    ┌───────────────────────┐
                    │  Python Data Generator │
                    │  (Synthetic Dataset)   │
                    └──────────┬────────────┘
                               │
                               ▼
                    ┌───────────────────────┐
                    │      CSV Files        │
                    │ Customers             │
                    │ Accounts              │
                    │ Branches              │
                    │ Transactions          │
                    └──────────┬────────────┘
                               │
                               ▼
                    ┌───────────────────────┐
                    │ Snowflake Stage       │
                    │ BANK_STAGE            │
                    └──────────┬────────────┘
                               │
                               ▼
                    ┌───────────────────────┐
                    │ RAW Schema            │
                    │ Customers             │
                    │ Accounts              │
                    │ Branches              │
                    │ Transactions          │
                    └──────────┬────────────┘
                               │
                               ▼
                    ┌───────────────────────┐
                    │ Analytics Schema      │
                    │ Executive Summary     │
                    │ Customer 360          │
                    │ Branch Performance    │
                    │ Transaction Analytics │
                    │ Fraud Analytics       │
                    └──────────┬────────────┘
                               │
                               ▼
                    ┌───────────────────────┐
                    │ Power BI              │
                    │ Executive Dashboard   │
                    │ Customer Analytics    │
                    │ Transaction Insights  │
                    │ Fraud Intelligence    │
                    └───────────────────────┘
```