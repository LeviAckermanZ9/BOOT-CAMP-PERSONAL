Let's dive into more advanced features and capabilities of Pandas:

### Advanced DataFrame Manipulations

#### MultiIndex (Hierarchical Indexing)
Pandas supports hierarchical indexing, which allows you to work with higher-dimensional data in a lower-dimensional DataFrame.

1. **Creating a MultiIndex:**
    ```python
    arrays = [
        ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
        ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']
    ]
    index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
    df = pd.DataFrame(np.random.randn(8, 4), index=index, columns=['A', 'B', 'C', 'D'])
    print(df)
    ```

2. **Accessing Data in a MultiIndex:**
    ```python
    print(df.loc['bar'])
    print(df.loc['bar', 'one'])
    ```

3. **Unstacking and Stacking:**
    ```python
    unstacked = df.unstack()
    print(unstacked)
    restacked = unstacked.stack()
    print(restacked)
    ```

#### Pivot Tables
Pivot tables are used to summarize data.

1. **Creating a Pivot Table:**
    ```python
    data = {
        'A': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'one', 'two', 'two', 'one', 'one', 'two', 'two'],
        'C': ['small', 'large', 'large', 'small', 'small', 'small', 'small', 'large', 'large'],
        'D': [1, 2, 2, 3, 3, 4, 5, 6, 7],
        'E': [2, 4, 5, 5, 6, 7, 8, 9, 9]
    }
    df = pd.DataFrame(data)
    pivot = df.pivot_table(values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum)
    print(pivot)
    ```

#### Advanced Grouping
Grouping data with more complex aggregations and transformations.

1. **Multiple Aggregation Functions:**
    ```python
    data = {
        'A': ['foo', 'foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'one', 'two', 'two', 'one', 'one', 'two', 'two'],
        'C': ['small', 'large', 'large', 'small', 'small', 'small', 'small', 'large', 'large'],
        'D': [1, 2, 2, 3, 3, 4, 5, 6, 7],
        'E': [2, 4, 5, 5, 6, 7, 8, 9, 9]
    }
    df = pd.DataFrame(data)
    grouped = df.groupby(['A', 'B'])
    print(grouped.agg({'D': ['sum', 'mean'], 'E': ['count', 'mean']}))
    ```

2. **Transform:**
    ```python
    df['D_transformed'] = df.groupby('A')['D'].transform(lambda x: x - x.mean())
    print(df)
    ```

3. **Apply:**
    ```python
    def normalize(x):
        return (x - x.mean()) / x.std()

    normalized = df.groupby('A').apply(lambda x: normalize(x['D']))
    print(normalized)
    ```

### Time Series and Date Functionality
Pandas provides extensive capabilities for working with time series data.

1. **Date Range Generation:**
    ```python
    date_range = pd.date_range(start='1/1/2020', end='1/10/2020')
    print(date_range)
    ```

2. **Shifting and Lagging:**
    ```python
    df = pd.DataFrame({
        'Date': pd.date_range('20230101', periods=6),
        'Value': np.random.randn(6)
    })
    df['Shifted'] = df['Value'].shift(1)
    print(df)
    ```

3. **Rolling and Expanding Windows:**
    ```python
    df['Rolling_Mean'] = df['Value'].rolling(window=2).mean()
    print(df)
    ```

4. **Resampling:**
    ```python
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2020', periods=1000))
    monthly_mean = ts.resample('M').mean()
    print(monthly_mean)
    ```

### Advanced Data Input/Output
Pandas can read from and write to a variety of file formats.

1. **Reading and Writing to SQL Databases:**
    ```python
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:')
    df.to_sql('data', engine)
    sql_df = pd.read_sql('data', engine)
    print(sql_df)
    ```

2. **Reading and Writing to Excel Files:**
    ```python
    df.to_excel('data.xlsx', sheet_name='Sheet1')
    excel_df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
    print(excel_df)
    ```

### Advanced Visualization
Pandas integrates with Matplotlib and Seaborn for advanced visualization.

1. **Box Plot:**
    ```python
    df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
    df.plot.box()
    ```

2. **Scatter Plot Matrix:**
    ```python
    pd.plotting.scatter_matrix(df, alpha=0.2)
    ```

3. **Time Series Plot:**
    ```python
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2020', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    ```

### Performance Tips
1. **Using Efficient Data Types:**
    ```python
    df['int_column'] = df['int_column'].astype('int32')
    df['float_column'] = df['float_column'].astype('float32')
    ```

2. **Optimizing Apply:**
    ```python
    df['new_column'] = df['column'].apply(np.sqrt)
    ```

3. **Using NumPy Functions:**
    ```python
    df['new_column'] = np.sqrt(df['column'])
    ```

### Conclusion
These examples cover more advanced features and functionalities of Pandas, including hierarchical indexing, pivot tables, advanced grouping, time series manipulation, advanced I/O, and visualization techniques. For more details and examples, the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/) is an excellent resource.

# THANK YOU