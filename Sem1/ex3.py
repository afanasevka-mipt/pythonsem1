import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-120, 120, 0.1)
plt.plot(x, (np.log((x**2 + 1)*(np.exp(-1*(abs(x)/10)))) / np.log(1+np.tan(1/(1 + (np.sin(x))**2)))))
plt.show()