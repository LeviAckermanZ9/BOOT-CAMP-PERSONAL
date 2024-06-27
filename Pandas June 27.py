Pandas is a powerful library for data manipulation and analysis in Python. It provides data structures like DataFrame and Series, which are designed to handle structured data. Below is more on Pandas:

### Installation
First, ensure you have Pandas installed. You can install it using pip:
```bash
pip install pandas
```

### Importing Pandas
```python
import pandas as pd
```

### Data Structures

#### Series
A Series is a one-dimensional array-like object containing an array of data and an associated array of data labels, called its index.

1. **Creating a Series:**
    ```python
    series = pd.Series([1, 2, 3, 4, 5])
    print(series)
    ```

2. **Series with Custom Index:**
    ```python
    series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
    print(series)
    ```

3. **Accessing Series Elements:**
    ```python
    print(series['a'])
    print(series[['a', 'c', 'e']])
    ```

#### DataFrame
A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).

1. **Creating a DataFrame:**
    ```python
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]
    }
    df = pd.DataFrame(data)
    print(df)
    ```

2. **Creating a DataFrame from a List of Dictionaries:**
    ```python
    data = [
        {'Name': 'Alice', 'Age': 25, 'Salary': 50000},
        {'Name': 'Bob', 'Age': 30, 'Salary': 60000},
        {'Name': 'Charlie', 'Age': 35, 'Salary': 70000}
    ]
    df = pd.DataFrame(data)
    print(df)
    ```

### Basic DataFrame Operations
1. **Inspecting Data:**
    ```python
    print(df.head())  # First 5 rows
    print(df.tail())  # Last 5 rows
    print(df.info())  # Info about DataFrame
    print(df.describe())  # Summary statistics
    ```

2. **Selecting Columns:**
    ```python
    print(df['Name'])
    print(df[['Name', 'Age']])
    ```

3. **Selecting Rows:**
    ```python
    print(df.loc[0])  # By label
    print(df.iloc[0])  # By position
    ```

4. **Filtering Rows:**
    ```python
    filtered_df = df[df['Age'] > 30]
    print(filtered_df)
    ```

5. **Adding a New Column:**
    ```python
    df['Bonus'] = df['Salary'] * 0.1
    print(df)
    ```

6. **Dropping Columns and Rows:**
    ```python
    df_dropped = df.drop(['Bonus'], axis=1)  # Drop column
    print(df_dropped)
    df_dropped = df.drop([0], axis=0)  # Drop row
    print(df_dropped)
    ```

### Data Cleaning
1. **Handling Missing Data:**
    ```python
    df_with_nan = df.copy()
    df_with_nan.loc[1, 'Age'] = None
    print(df_with_nan)

    df_filled = df_with_nan.fillna(0)
    print(df_filled)

    df_dropped = df_with_nan.dropna()
    print(df_dropped)
    ```

2. **Replacing Values:**
    ```python
    df_replaced = df.replace(60000, 65000)
    print(df_replaced)
    ```

### Data Aggregation and Grouping
1. **Group By:**
    ```python
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
        'Year': [2020, 2020, 2020, 2021, 2021, 2021],
        'Salary': [50000, 60000, 70000, 52000, 62000, 72000]
    }
    df = pd.DataFrame(data)
    print(df)

    grouped = df.groupby('Name')
    print(grouped.mean())
    ```

2. **Aggregating Functions:**
    ```python
    print(grouped.agg({'Salary': ['mean', 'sum']}))
    ```

### Merging and Joining
1. **Merging DataFrames:**
    ```python
    df1 = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]
    })
    df2 = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'David'],
        'Salary': [50000, 60000, 70000]
    })
    merged = pd.merge(df1, df2, on='Name', how='inner')
    print(merged)
    ```

2. **Joining DataFrames:**
    ```python
    df1 = df1.set_index('Name')
    df2 = df2.set_index('Name')
    joined = df1.join(df2, how='inner')
    print(joined)
    ```

### Time Series
Pandas has robust support for working with time series data.

1. **Creating a Time Series:**
    ```python
    dates = pd.date_range('20210101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    ```

2. **Resampling:**
    ```python
    ts = df['A']
    resampled = ts.resample('D').mean()
    print(resampled)
    ```

### Visualization
Pandas integrates well with Matplotlib for plotting.

1. **Basic Plotting:**
    ```python
    df.plot()
    ```

2. **Plotting Specific Columns:**
    ```python
    df['A'].plot()
    ```

3. **Histogram:**
    ```python
    df['A'].hist()
    ```

### Conclusion
These examples cover the basics and some advanced features of Pandas. For more details, the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/) Check the link out. 

# THANK YOU