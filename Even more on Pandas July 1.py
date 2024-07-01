
### Advanced Data Cleaning and Transformation

#### Handling Missing Data

1. **Forward Fill and Backward Fill:**
    ```python
    df = pd.DataFrame({
        'A': [1, np.nan, 3, 4, np.nan, 6],
        'B': [np.nan, 2, np.nan, 4, 5, np.nan]
    })
    df_ffill = df.fillna(method='ffill')
    print(df_ffill)
    df_bfill = df.fillna(method='bfill')
    print(df_bfill)
    ```

2. **Interpolating Missing Data:**
    ```python
    df_interpolated = df.interpolate()
    print(df_interpolated)
    ```

3. **Dropping Rows or Columns with Missing Data:**
    ```python
    df_dropped_rows = df.dropna(axis=0)
    print(df_dropped_rows)
    df_dropped_columns = df.dropna(axis=1)
    print(df_dropped_columns)
    ```

#### String Manipulation
Pandas provides powerful string manipulation capabilities through the `.str` accessor.

1. **Basic String Operations:**
    ```python
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
        'City': ['New York', 'Los Angeles', 'San Francisco', 'Seattle', 'Chicago']
    })
    df['Name_upper'] = df['Name'].str.upper()
    print(df)
    df['City_split'] = df['City'].str.split()
    print(df)
    ```

2. **String Matching and Replacing:**
    ```python
    df['City_contains_space'] = df['City'].str.contains(' ')
    print(df)
    df['City_replaced'] = df['City'].str.replace(' ', '_')
    print(df)
    ```

#### Working with Dates and Times
Pandas provides extensive functionality for parsing, formatting, and manipulating dates and times.

1. **Parsing Dates:**
    ```python
    df = pd.DataFrame({
        'Date': ['2023-01-01', '2023-02-01', '2023-03-01']
    })
    df['Date'] = pd.to_datetime(df['Date'])
    print(df)
    ```

2. **Extracting Date Components:**
    ```python
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    print(df)
    ```

3. **Date Arithmetic:**
    ```python
    df['Next_Month'] = df['Date'] + pd.DateOffset(months=1)
    print(df)
    ```

### Working with Large Datasets
Handling large datasets efficiently requires a combination of optimization techniques and sometimes using libraries designed for big data.

1. **Reading Data in Chunks:**
    ```python
    chunk_iter = pd.read_csv('large_file.csv', chunksize=1000)
    for chunk in chunk_iter:
        # Process each chunk
        print(chunk.head())
    ```

2. **Using Dask for Larger-than-Memory Data:**
    ```python
    import dask.dataframe as dd
    ddf = dd.read_csv('large_file.csv')
    print(ddf.head())
    ```

### Advanced GroupBy Operations

1. **Grouping by Multiple Columns:**
    ```python
    df = pd.DataFrame({
        'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': [1, 2, 3, 4, 5, 6]
    })
    grouped = df.groupby(['A', 'B']).sum()
    print(grouped)
    ```

2. **Custom Aggregation Functions:**
    ```python
    def custom_agg(series):
        return series.max() - series.min()

    grouped = df.groupby('A').agg({'C': custom_agg})
    print(grouped)
    ```

3. **Cumulative Operations:**
    ```python
    df['C_cumsum'] = df.groupby('A')['C'].cumsum()
    print(df)
    ```

### Advanced Merging and Joining

1. **Merging on Multiple Columns:**
    ```python
    df1 = pd.DataFrame({
        'key1': ['A', 'B', 'C', 'D'],
        'key2': [1, 2, 3, 4],
        'value': [10, 20, 30, 40]
    })
    df2 = pd.DataFrame({
        'key1': ['A', 'B', 'C', 'D'],
        'key2': [1, 2, 3, 4],
        'value': [100, 200, 300, 400]
    })
    merged = pd.merge(df1, df2, on=['key1', 'key2'], suffixes=('_left', '_right'))
    print(merged)
    ```

2. **Merging with Different Join Types:**
    ```python
    df_left = pd.DataFrame({
        'key': ['A', 'B', 'C'],
        'value_left': [1, 2, 3]
    })
    df_right = pd.DataFrame({
        'key': ['B', 'C', 'D'],
        'value_right': [4, 5, 6]
    })
    outer_join = pd.merge(df_left, df_right, on='key', how='outer')
    print(outer_join)
    inner_join = pd.merge(df_left, df_right, on='key', how='inner')
    print(inner_join)
    ```

### Advanced Visualization

1. **Seaborn Integration:**
    ```python
    import seaborn as sns
    df = pd.DataFrame({
        'A': np.random.randn(100),
        'B': np.random.randn(100),
        'C': np.random.randn(100)
    })
    sns.pairplot(df)
    ```

2. **Plotting with Matplotlib:**
    ```python
    import matplotlib.pyplot as plt
    df = pd.DataFrame({
        'A': np.random.randn(1000).cumsum(),
        'B': np.random.randn(1000).cumsum()
    })
    df.plot()
    plt.show()
    ```

3. **Geospatial Plotting:**
    ```python
    import geopandas as gpd
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world.plot()
    plt.show()
    ```

### Performance Optimization

1. **Vectorized Operations:**
    ```python
    df = pd.DataFrame({
        'A': np.random.randn(1000000),
        'B': np.random.randn(1000000)
    })
    df['C'] = df['A'] + df['B']  # Vectorized, efficient
    ```

2. **Using Categorical Data:**
    ```python
    df = pd.DataFrame({
        'A': ['foo', 'bar', 'foo', 'bar'] * 1000000,
        'B': np.random.randn(4000000)
    })
    df['A'] = df['A'].astype('category')
    ```

3. **Using `.apply()` Efficiently:**
    ```python
    def complex_function(x):
        return x**2 - np.log(x + 1)

    df['D'] = df['C'].apply(complex_function)
    ```

### Conclusion

# THANK YOU