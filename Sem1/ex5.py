import numpy as np
import matplotlib.pyplot as plt
x = [1.0, 2.0, 3.0, 4.0, 5.0]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
pl1 = []
pl2 = []
p, v = np.polyfit(x, y, deg=1, cov=True)
p1 = str(np.poly1d(p)).split()
print(p1)
for i in x:
    pl1.append(float(p1[0])*i+float(p1[3]))
plt.plot(x, pl1, color='green', label='$Approximation\ by\ first\ degree$')
p, v = np.polyfit(x, y, deg=2, cov=True)
p2 = str(np.poly1d(p)).split()
print(p2)
for i in x:
    pl2.append(float(p2[1])*i - float(p2[4])*i + float(p2[-1]))
plt.plot(x, pl2, color='red', label='$Approximation\ by\ second\ degree$')
plt.errorbar(x, y, xerr=0.05, yerr=0.1, color='blue')
plt.legend(loc='best', fontsize=13)
plt.grid()
plt.show()