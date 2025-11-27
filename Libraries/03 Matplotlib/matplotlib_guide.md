# 📊 Matplotlib Cheat Sheet

## 📌 Introduction
**Matplotlib** is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is widely used in data analysis and scientific computing.

Install it using:
```bash
pip install matplotlib
```

Import it using:
```python
import matplotlib.pyplot as plt
```

---

## 🧱 Basic Components
- **Figure**: The entire window where your plots will be displayed.
- **Axes**: A part of the figure where data is plotted (can be multiple).
- **Axis**: X and Y axis of a plot.

```python
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
```

---

## 📈 Basic Plotting
```python
x = [1, 2, 3, 4, 5]
y = [10, 5, 7, 12, 8]

plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
```

### 🔹 Common Plot Types
```python
plt.plot(x, y)            # Line Plot
plt.scatter(x, y)         # Scatter Plot
plt.bar(x, y)             # Bar Plot
plt.barh(x, y)            # Horizontal Bar Plot
plt.hist(data)            # Histogram
plt.boxplot(data)         # Box Plot
plt.pie(data)             # Pie Chart
plt.stackplot(x, y)       # Stacked Plot
plt.fill_between(x, y)    # Fill Between
plt.errorbar(x, y)        # Error Bar
plt.step(x, y)            # Step Plot
```

---

## 🎨 Customization
```python
plt.plot(x, y, color='red', linestyle='--', marker='o', label='Data')
plt.legend()              # Show legend
plt.grid(True)            # Show grid
plt.xlim(min, max)        # Set X-axis limits
plt.ylim(min, max)        # Set Y-axis limits
plt.xticks([...])         # Customize ticks on X-axis
plt.yticks([...])         # Customize ticks on Y-axis
```

### 📋 Titles and Labels
```python
plt.title("Main Title")
plt.suptitle("Super Title")
plt.xlabel("X Label")
plt.ylabel("Y Label")
```

---

## 📊 Subplots
```python
plt.subplot(1, 2, 1)   # 1 row, 2 columns, plot 1
plt.plot(x, y)

plt.subplot(1, 2, 2)   # plot 2
plt.bar(x, y)

plt.tight_layout()
plt.show()
```

Or using object-oriented approach:
```python
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].bar(x, y)
axs[1, 0].hist(data)
axs[1, 1].scatter(x, y)
```

---

## ✍️ Annotations and Text
```python
plt.annotate("Peak", xy=(3, 12), xytext=(4, 13),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.text(2, 10, "Note this point", fontsize=12)
```

---

## 🌈 Colormaps
```python
plt.imshow(data, cmap='viridis')
plt.colorbar()
```

---

## 🧩 3D Plotting
```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot3D(x, y, z)
```

---

## 🔁 Animation Support
```python
from matplotlib.animation import FuncAnimation
```
Use for dynamic, animated charts in Jupyter or GUIs.

---

## 📎 Pandas and NumPy Integration
```python
import pandas as pd

df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
df.plot(x='x', y='y', kind='line')
```

---

## 💾 Save the Plot
```python
plt.savefig("myplot.png")
plt.savefig("myplot.pdf")
plt.savefig("myplot.svg")
```

---

## 🧪 Interactive Mode
```python
%matplotlib inline     # For static plots in notebooks
%matplotlib notebook   # For interactive plots
```

---

## 📚 Commonly Used Functions & Methods
- `plt.plot()`
- `plt.scatter()`
- `plt.bar()` / `plt.barh()`
- `plt.hist()`
- `plt.pie()`
- `plt.boxplot()`
- `plt.errorbar()`
- `plt.step()`
- `plt.fill_between()`
- `plt.stackplot()`
- `plt.legend()`
- `plt.grid()`
- `plt.title()` / `plt.suptitle()`
- `plt.xlabel()` / `plt.ylabel()`
- `plt.xlim()` / `plt.ylim()`
- `plt.xticks()` / `plt.yticks()`
- `plt.subplot()` / `plt.subplots()`
- `plt.tight_layout()`
- `plt.savefig()`
- `plt.show()`
- `plt.annotate()` / `plt.text()`
- `plt.imshow()` / `plt.colorbar()`
- `ax.plot3D()` / `Axes3D`

---

## 🧠 Advanced Tips
- Use `fig, ax = plt.subplots()` for more control.
- Use `plt.style.use('ggplot')` or other styles.
- Combine with `pandas` for direct plotting: `df.plot()`
- Use `ax.set_title()`, `ax.set_xlabel()`, etc., for OO-style plots
- Use animations for dynamic visualizations

---

## 🧪 Example: Multiple Lines
```python
plt.plot(x, y, label='Line 1')
plt.plot(x, [i*2 for i in y], label='Line 2')
plt.legend()
plt.show()
```

---

## ❓ Common Interview/Practice Questions
1. How do you create multiple subplots in one figure?
2. How can you add a legend to the plot?
3. How to change the line style and color in a plot?
4. What’s the difference between `plt.plot()` and `plt.scatter()`?
5. How do you save a plot to a file?
6. How to display multiple graphs in the same window?
7. How do you plot directly from a pandas DataFrame?
8. What are different figure customization methods?
9. How to handle overlapping plots?
10. How to use Matplotlib with Seaborn?
11. How to annotate specific data points?
12. What are interactive plotting options in Jupyter?
13. What are the ways to create 3D plots in matplotlib?
14. How can you animate a chart using Matplotlib?

---

## 🔚 Conclusion
Matplotlib is a powerful tool for data visualization in Python. Mastering it is crucial for any data scientist or ML engineer.

> "A picture is worth a thousand rows of data."
