import numpy as np
import matplotlib.pyplot as plt
# for x^2-2x+1
def f(x):
    return (x**2+1)/2

x = np.linspace(0.69,1,100)
plt.plot(x,x,x,f(x))