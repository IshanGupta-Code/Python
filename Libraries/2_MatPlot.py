import numpy as np
import matplotlib.pyplot as plt

years = np.array([2005, 2006, 2007, 2011])
grade = np.array([54.05, 71, 69, 76])
plt.plot(years, grade, marker = "o")
plt.xlabel("Years")
plt.ylabel("Grade")
plt.title("My Academic Grades")
plt.grid()
plt.show()

# PIE
x = np.array([90, 75, 80, 65])
plt.title("Title")
name = np.array(["Python", "Java","React", "C"])
plt.pie(x, labels=name, shadow=True)
plt.legend()

# plt.xticks(name)
plt.show()

#  BAR
plt.bar(years, grade)
plt.grid()
plt.show()

# Scatter
plt.scatter(years, grade, marker="")
plt.grid()
plt.show()






