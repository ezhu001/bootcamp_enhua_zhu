## Data Storage

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
