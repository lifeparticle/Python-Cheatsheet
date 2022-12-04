# Data types

## Identify data types

```py
df = pd.DataFrame({'id': ["1"]})
df.dtypes # name    object
```

## Convert data types

```py
df['id'] = df['id'].astype('int')
df.dtypes # id    int64
```

| Python data type | Panda data type | Example       |
| ---------------- | --------------- |---------------|
| float            | float64         | 3.1416        |
| int              | int64           | 2, 3, 5       |
| datetime         | datetime64[ns]  | '2007-07-13'  |
| string           | object          | 'A', 'E', 'I' |

# Data formats

| Data format | Read data       | Write data    |
| ----------- | --------------- | ------------- |
| csv         | pd.read_csv()   | pd.to_csv()   |
| json        | pd.read_json()  | pd.to_json()  |
| excel       | pd.read_excel() | pd.to_excel() |
| sql         | pd.read_sql()   | pd.to_sql()   |


# Data wrangling / data cleaning / data pre-processing

## Add values

Add 1 to each entry of a column.

```py
dataframe['column 1'] = dataframe['column 1'] + 1
```

## Missing values

Missing values could be represented as `N/A`, empty cell, etc.

### Drop missing values

- Drop the variable
- Drop the data entry

```py
dataframe.dropna(subset=['column 1'], axis=0, inplace=True) # axis=0 drops the entire row
dataframe.dropna(subset=['column 1'], axis=1, inplace=True) # axis=1 drops the entire column
```

### Replace missing values

- Use an average
- Use frequency

```py
mean = dataframe['column 1'].mean()
dataframe['column 1'].re[place(np,nan, mean)
```

### Leave it as missing values


# Data formatting

Non-formatted -> Formatted
SYD -> Sydney
S.Y.D -> Sydney

hard to compare -> easy to compare
hard to aggregate -> easy to aggregate

# Data normalizations

## Feature scaling


$$
x_{new} = x_old/x_max
$$

## Min-Max

$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}
$$

## Z-score

$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}
$$




## Rename column name

```py
dataframe.rename(columns={'column 1': 'column 2'}, inplace=True)
```

# Methods

## Show data types.

```py
dataframe.dtypes
```

## Show statistical information and skips rows and columns that do not contain numbers.

```py
dataframe.describe()
dataframe[['column 1', 'column 2']].describe()
```

## Show statistical information for all columns.

```py
dataframe.describe(include="all")
```

## Show top and botton 30 rows.

```py
dataframe.info()
```

## Show first 5 rows

```py
dataframe.head(5)
```

## Show last 5 rows

```py
dataframe.tail(5)
```

## Create and set headers

```py
headers = ["header1","header3","header3"]
dataframe.columns = headers
```

## Show name of the colmuns

```py
dataframe.columns
```

# Resources

1. [Standardization vs Normalization Clearly Explained!](https://www.youtube.com/watch?v=sxEqtjLC0aM)