import matplotlib.pyplot as plt
import numpy as np

x = ([1, 2, 3, 4, 5])
y = ([10, 20, 30, 40, 50])

plt.title("My Graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x,y, marker = "o", ms=20, mec="purple", mfc="pink", color="blue",
         linewidth=10, linestyle="dotted")
plt.show()