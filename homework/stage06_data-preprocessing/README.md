\# Data Cleaning Functions in which I prepared documentation strings and the assumptions; they are all included in the README.md
---



\## `fill\_missing\_median(df, columns=None)`



Fill missing numeric values with the median of each column.



\*\*Parameters\*\*

\- `df` (`pd.DataFrame`): Input DataFrame.  

\- `columns` (`list`, optional): Columns to fill. If `None`, all numeric columns are filled.  



\*\*Returns\*\*

\- `pd.DataFrame`: DataFrame with missing values in specified numeric columns filled.  



\*\*Assumptions\*\*

\- Only numeric columns for filling with medians.

\- Non-numeric columns are ignored in general.

\- A full NaN column will leade to any fill be NaN. 



---



\## `drop\_missing(df, threshold=0.5)`



Drop columns whose proportion of missing values exceeds a threshold.  



\*\*Parameters\*\*

\- `df` (`pd.DataFrame`): Input DataFrame.  

\- `threshold` (`float`, default=0.5): Maximum fraction of missing values allowed per column.  



\*\*Returns\*\*

\- `pd.DataFrame`: DataFrame with high-missingness columns removed.  



\*\*Assumptions\*\*

\- Threshold is stated, like 50% here.

\- Entire columns are dropped, not individual rows.

---



\## `normalize\_data(df, columns=None)`



Normalize numeric values to `\[0, 1]` range using Min-Max scaling.  



\*\*Parameters\*\*

\- `df` (`pd.DataFrame`): Input DataFrame.  

\- `columns` (`list`, optional): Columns to normalize. If `None`, all numeric columns are normalized.  



\*\*Returns\*\*

\- `pd.DataFrame`: DataFrame with specified columns normalized between 0 and 1.  



\*\*Assumptions\*\*

\- Works only on numeric columns; raise errors for non-numeric ones.

\- If a column has constant values, MinMaxScaler will scale all values to 0. 



---

