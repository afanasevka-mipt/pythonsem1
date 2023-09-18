import matplotlib.pyplot as plt
import numpy as np
with plt.xkcd():
    f = input()
    x = np.arange(-100, 100, 1)
    y = [eval(f) for x in x]
    plt.plot(x, y)
    plt.show()
