# Next-Day Stock Rise Probability Predictor

## Problem Statement 

<1–2 paragraphs: what problem & why it matters> 

This project aims to predict the probability that a given stock’s price will rise the next trading day based on its historical price and volume data. Specifically, when given the input of an arbitrary stock ticket alongside its key daily prices (Open, Close, High, Low) and Volume for the last 365 calendar days, we want to output a number in the range of 0 to 1 indicating the likelihood that the stock’s closing price tomorrow will exceed today’s closing price. It assists in predicting stock's short-term performance.

## Stakeholder & User

<Who decides? Who uses the output? Timing & workflow context> 

Primary users identified are individual, short-term (or even over-night) stock investors who are eager to predict how well a single stock behaves and to make the decision on whether to buy it. It provides a quantitative, clear, and intuitive measurement on how good the stock is for now given its past performance, and can be easily interpreted. The timeframe is usually daily as described in problem statement.

## Useful Answer & Decision 

<Descriptive / Predictive / Causal; metric; artifact to deliver> 

Predictive - it intends to predict whether the stock price of a given stock is likely to rise in the next trading day given its performance over the last 365 calendar days.

Metric - it predicts by providing a number between 0 and 1, indicating the likelihood that the stock's closing price in the next trading day will exceed today's closing price. However, I am also thinking that it might be artifact to some extent.

Artifact - It will be delivered to users as a program (which is an artifact) that allow the user to input a stock ticket and to obtain prediction on the stock's future performance.

## Assumptions & Constraints 

<Bullets: data availability, capacity, latency, compliance, etc.> 

Data availability - readily available but is not always free and requires some work: Bloomberg official API, yfinance Library in Python, (or if for stocks on Shanghai Stock Exchange / Shenzhen Stock Exchange, Akshare is also a free and powerful tool).

Capacity - Assumed that there is no problem with the capacity, as daily data for thousands of stocks in the past few years would not be too large a number.

Latency - Assumed that there is neither requirement nor tangible constraints on latency, as it is not for high-frequency trading.

## Known Unknowns / Risks 

<Bullets: what’s uncertain; how you’ll test or monitor> 

Confounding factors - many factors other than the stock's past performance are highly correlated with its change of price. Certainly we cannot extract all factors.

Test and monitor - Backtesting with 6~8 years of data would help us to refine the model. Also, after providing the probability of the stock's price to go up next trading day, we will also compare outcomes with the predicted probability in order to measure the performance of such prediction.

## Lifecycle Mapping 

Goal → Stage → Deliverable - <Goal A> → Problem Framing & Scoping (Stage 01) → <Deliverable X> - ... 

1. Predict next-day stock price movement​​ → Problem Framing & Scoping (Stage 01) → Project Scoping Document

​​2. Build predictive model​​ → Data Collection & Preprocessing (Stage 02) → Datasets and Program

3. Improve model​​ → Model Development & Testing (Stage 03) → Trained Model and Backtesting Results

4. Deploy for user access​​ → Implementation and Monitoring (Stage 04) → Probability Prediction program ready to use

## Repo Plan 
/data/raw, /data/processed, /src/, /notebooks/, /docs/ note that data is under notebooks as it would be hard to link directories on different levels

## Data Fetching and Storage Updates
Folder Structure
data/raw/ Contains csv directly taken as dataframe

data/processed/ Contains parquet files as processed data

File Formats
CSV (.csv) is primarily used for both raw and processed data because:

Widely applied and useful
Easy to integrate with Python’s environment and libraries
**Parquet is used for processed data as it is efficient and can be used for columnar storage (this answer was found on website/GPT)

Environment Variables for I/O
The project relies on environment variables (defined in a .env file) to manage file paths and API keys without hardcoding sensitive or system-specific information.
For example:

DATA_RAW=./data/raw
DATA_PROCESSED=./data/processed

# Data Sources
This project uses ALPHAVANTAGE and Yahoo Finance for data fetching

---

## API

- **Data Sources:**  
  - [Alphavantage](avantage.co/support/#api-key)
  - [Yahoo Finance](https://finance.yahoo.com/quote/AAPL/history/)  

- **Endpoints / URLs:**  
  - `avantage.co/support/#api-key`
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
# Assumptions and explanation for data cleaning and preprocessing:

- 1. Missing values are forward-filled (assume that the price did not change in case of price missing; it might be a non-trading day)

- 2. Outliers removed for apparently wrong value, as it would be almost not reasonable to have price that fluctuate this much. But 
I am also thinking of not to remove outliers for some stocks known to be highly volatile

- 3. Normalized volumes to reflect change in volumes in a more clear way

- 4. Adding the "returns" for showing how price changes alone the way, which would be useful in future processing of data.
(I asked GPT for some inspirations on this)
