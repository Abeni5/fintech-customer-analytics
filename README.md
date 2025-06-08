# Customer Experience Analytics for Fintech Apps
## Task 1: Data Collection and Preprocessing
- Scraped 1,200 reviews (400 per bank) from Google Play Store for CBE, BOA, and Dashen Bank.
- Preprocessed data to remove duplicates, resulting in 800 unique reviews due to possible app ID overlap.
- Output: `data/bank_reviews_cleaned.csv`.
- KPIs: 800 unique reviews, 0% missing data.
## Task 1 Notes
- CBE and BOA may have used the same app ID (`com.combanketh.mobilebanking`), causing duplicates. Plan to verify BOA’s app ID (e.g., `et.com.bankofabyssinia.boa`) for final submission.