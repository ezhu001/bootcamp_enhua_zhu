## Data Storage (Updated 08/17/2025)

### Folder Structure
- data/raw/ 
  Contains csv directly taken as dataframe 

- data/processed/
  Contains parquet files as processed data

### File Formats
- **CSV (`.csv`)** is primarily used for both raw and processed data because:  
  - Widely applied and useful 
  - Easy to integrate with Python’s environment and libraries

- **Parquet is used for processed data as it is efficient and can be used for columnar storage (this answer was found on website/GPT) 

### Environment Variables for I/O
The project relies on environment variables (defined in a `.env` file) to manage file paths and API keys without hardcoding sensitive or system-specific information.  
For example:
```env
DATA_RAW=./data/raw
DATA_PROCESSED=./data/processed

# Data Sources

This project uses two main approaches to obtain financial and corporate data: **APIs** and **Web Scraping**. Each approach has its own advantages, risks, and considerations.

---

## API

- **Data Sources:**  
  - [Finnhub](https://finnhub.io/docs/api)  
  - [Yahoo Finance](https://finance.yahoo.com/quote/AAPL/history/)  

- **Endpoints / URLs:**  
  - `https://finnhub.io/api/v1/stock/candle`  
  - `https://finance.yahoo.com/quote/AAPL/history/`  

- **Parameters Collected:**  
  - `Date`  
  - `Open`  
  - `High`  
  - `Low`  
  - `Close`  
  - `Volume`  

- **Potential Issues:**  
  1. **Subscription requirements** – some APIs (e.g., Finnhub) may require a paid subscription for full access.  
  2. **URL changes** – APIs may update their endpoints, requiring code updates.  
  3. **Format changes** – while APIs generally provide structured and consistent formats (e.g., JSON), there is still some risk of format changes.  

---

## Scraping

- **Data Source:**  
  - [Wikipedia – List of largest companies by revenue](https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue)  

- **Parameters Collected:**  
  - `Rank`  
  - `Name`  
  - `Industry`  
  - `Revenue`  
  - `Profit`  
  - `Employees`  
  - `Headquarters`  
  - `State-owned`  
  - `Reference`  

- **Potential Issues:**  
  1. **Inconsistent formats** – HTML structures on Wikipedia can change, requiring frequent updates to the scraping logic.  
  2. **Policy changes** – scraping policies may change over time, and access may be restricted.  
  3. **Unclear usage rights** – unlike APIs, Wikipedia scraping may not always have clearly stated usage terms for downstream applications.  

---

## Summary

- **APIs** provide structured, reliable, and machine-friendly data, but may require subscriptions and be subject to endpoint changes.  
- **Scraping** is useful when APIs are unavailable, but it is more fragile and subject to website structure or policy changes.  

This project combines both methods to ensure data availability and coverage.  
