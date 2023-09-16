import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10, 10, 0.1)
plt.plot(x, x*x-x-6)
plt.plot(x, x*0)
plt.show()