import numpy as np
def urav(x: int) -> float:
    y = np.log((1/(np.e**(np.sin(x)+1)))/(1.25 + 1/x**15)) / np.log(1 + x**2)
    return y
print(urav(1))
print(urav(10))
print(urav(1000))
