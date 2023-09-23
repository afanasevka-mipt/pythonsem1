import numpy as np
import matplotlib.pyplot as plt
xsp = np.arange(-3, 3.01, 0.001)
n = 100
b = 0.36
a = 7
ysp = np.array([])
y = np.array([])
for x in xsp:
    for i in range(n):
        y = np.append(y, np.cos(np.pi*x*a**i)*b**i)
    sum_y = np.sum(y)
    ysp = np.append(ysp, sum_y)
    y = np.array([])
 
plt.plot(xsp, ysp)
plt.grid = True
plt.show()