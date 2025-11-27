# **NumPy Library – Python Cheat Sheet**

## **🔹 Installation**

To install NumPy, open your terminal and run:

```
pip install numpy
```

---

## **🔹 What is NumPy?**

NumPy (Numerical Python) is a powerful library used for:

* Working with large datasets.
* Performing mathematical and logical operations on arrays.
* Creating N-dimensional arrays.
* Supporting high-level mathematical functions.

---

## **🔹 Core NumPy Functions**

1. `np.array()` – Create a normal array.
2. `np.flip()` – Reverse the order of elements in an array.
3. `np.sort()` – Sort elements.
4. `np.zeros()` – Create an array filled with zeros.
5. `np.ones()` – Create an array filled with ones.
6. `np.full(shape, value)` – Fill array with a specific value.
7. `np.arange(start, stop, step)` – Generate a sequence.
8. `np.eye(n)` – Create an identity matrix.

---

## **🔹 Array Properties \& Info**

* `.shape` → Returns shape (rows, columns)
* `.size` → Number of elements
* `.ndim` → Number of dimensions
* `.dtype` → Data type of elements
* `.astype()` → Type conversion of elements

---

## **🔹 Arithmetic Operations on Arrays**

You can perform arithmetic operations directly:

```python
matrix = np.array(\[10, 20, 30, 40])
print(matrix + 20)
print(matrix \* 6)
print(matrix \*\* 2)
```

Operations supported: `+`, `-`, `\*`, `/`, `//`, `%`, `\*\*`

---

## **🔹 Aggregate Functions**

* `np.sum()` → Total sum of array
* `np.mean()` → Mean (average)
* `np.min()` → Minimum value
* `np.max()` → Maximum value
* `np.std()` → Standard deviation
* `np.var()` → Variance

---

## **🔹 Indexing and Slicing**

### **Basic Indexing**

* 1D: `arr\[index]`
* 2D: `arr\[row, column]`

### **Fancy Indexing**

```python
arr\[\[0, 1, 5]]  # Access multiple indices
```

### **Boolean Indexing**

```python
arr\[arr > 35]  # Filter based on condition
```

### **Slicing Syntax**

```python
arr\[start:stop:step]
```

---

## **🔹 Reshaping \& Flattening Arrays**

### **Reshaping**

* `arr.reshape(new\_shape)` – Change array shape without altering data.
* Doesn't create a copy, modifies the original.

### **Flattening**

* `.ravel()` – Returns 1D view (affects original array)
* `.flatten()` – Returns a copy (doesn't affect original)

---

## **🔹 Manipulating Arrays**

### **Insertion**

* `np.insert(array, index, value, axis)`

### **Appending**

* `np.append(array1, array2)`

### **Concatenation**

* `np.concatenate((array1, array2), axis)`

### **Deletion**

* `np.delete(array, index, axis)`

### **Stacking**

* `np.stack((arr1, arr2), axis)`
* `np.vstack((arr1, arr2))` – Vertical stack
* `np.hstack((arr1, arr2))` – Horizontal stack

### **Splitting**

* `np.split(array, num\_sections)`
* `np.vsplit(array, sections)`
* `np.hsplit(array, sections)`

---

## **🔹 Handling Missing or Infinite Values**

### **Missing Values**

* `np.isnan(array)` → Detects NaNs
* `np.nan\_to\_num(array)` → Replaces NaNs (default = 0)

### **Infinite Values**

* `np.isinf(array)` → Detects infinite values

---

## **📝 Note**

Avoid naming your Python file with predefined keywords like `numpy.py`, `math.py` etc.

---

## ✅ End of NumPy Quick Guide

