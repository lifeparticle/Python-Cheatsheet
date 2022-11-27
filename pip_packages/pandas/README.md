# Data types

| Python data type | Panda data type |
| ---------------- | --------------- |
| float            | float64         |
| int              | int64           |
| datetime         | datetime64[ns]  |
| string           | object          |

# Data formats

| Data format | Read data       | Write data    |
| ----------- | --------------- | ------------- |
| csv         | pd.read_csv()   | pd.to_csv()   |
| json        | pd.read_json()  | pd.to_json()  |
| excel       | pd.read_excel() | pd.to_excel() |
| sql         | pd.read_sql()   | pd.to_sql()   |

# Methods

Show data types.

```py
dataframe.dtypes
```

Show statistical information and skips rows and columns that do not contain numbers.

```py
dataframe.describe()
dataframe[['column 1', 'column 2'] ].describe()
```

Show statistical information for all columns.

```py
dataframe.describe(include="all")
```

Show top and botton 30 rows.

```py
dataframe.info()
```

Show first 5 rows

```py
dataframe.head(5)
```

Show last 5 rows

```py
dataframe.tail(5)
```

Create and set headers

```py
headers = ["header1","header3","header3"]
dataframe.columns = headers
```

Show name of the colmuns

```py
dataframe.columns
```
