
# 📊 Pandas Library - Complete Reference

## 🔰 Introduction

**Pandas** is a powerful open-source Python library used for data manipulation and analysis. It provides fast, flexible, and expressive data structures, like Series and DataFrame, designed to work with structured data seamlessly.

## 🚀 Installation

```bash
pip install pandas
```

---

## 🧱 Core Data Structures

### 1. **Series**
- One-dimensional labeled array.
```python
import pandas as pd
s = pd.Series([10, 20, 30])
```

### 2. **DataFrame**
- Two-dimensional labeled data structure.
```python
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
```

---

## 🛠️ Key Functions and Operations

### 🔹 Creating DataFrame

```python
df = pd.DataFrame({
    'Name': ['John', 'Jane'],
    'Marks': [85, 90]
})
```

### 🔹 Reading/Writing Data

```python
df = pd.read_csv('file.csv')
df.to_excel('output.xlsx')
```

### 🔹 Data Inspection

```python
df.head()         # First 5 rows
df.tail()         # Last 5 rows
df.info()         # Summary info
df.describe()     # Statistical summary
df.shape          # (rows, columns)
df.columns        # Column names
```

### 🔹 Indexing & Slicing

```python
df['Name']                # Column access
df.loc[0]                 # Row by label
df.iloc[0]                # Row by position
df[0:2]                   # Slicing rows
df[['Name', 'Marks']]     # Multiple columns
```

### 🔹 Filtering with Conditions

```python
df[df['Marks'] > 80]
```

### 🔹 String Length

```python
df['Name'].str.len()  # To get the length of the name
```

### 🔹 Adding/Modifying/Deleting Columns

```python
df['Grade'] = ['A', 'A+']
df['Marks'] = df['Marks'] + 5
df.drop('Grade', axis=1, inplace=True)
```

### 🔹 Handling Missing Data

```python
df.isnull()
df.dropna()
df.fillna(0)
```

---

## 📊 Data Aggregation & Grouping

```python
df.groupby('Gender').mean()
df['Marks'].sum()
df['Marks'].min()
df['Marks'].max()
```

---

## 🔄 Sorting and Reordering

```python
df.sort_values(by='Marks')
df.sort_index()
```

---

## 🧹 Cleaning and Transforming Data

```python
df['Name'] = df['Name'].str.upper()
df.rename(columns={'Marks': 'Score'}, inplace=True)
```

---

## 🔁 Merging and Joining

```python
pd.merge(df1, df2, on='ID')
pd.concat([df1, df2])
```

---

## 📌 Time Series Handling

```python
pd.date_range(start='2024-01-01', periods=10)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
```

---

## 🔍 Important Interview Questions

1. What is the difference between Series and DataFrame?
2. How does Pandas handle missing data?
3. Explain `loc` vs `iloc`.
4. How can you merge two DataFrames?
5. What are different ways to filter rows in a DataFrame?
6. How to handle large datasets efficiently using Pandas?
7. What are lambda functions and how are they used in Pandas?
8. What is broadcasting in Pandas?
9. What is the difference between `apply()` and `map()`?
10. How do you handle time series data in Pandas?

---

## ✅ Conclusion

Pandas is an essential tool in any data scientist's toolkit. From simple CSV reading to complex data wrangling and analysis, Pandas handles it all with ease.

> **Pro Tip**: Use Pandas along with NumPy and Matplotlib/Seaborn to build powerful data pipelines.

---
