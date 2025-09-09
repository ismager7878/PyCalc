import sympy as sp
from sympy import pprint

import numpy as np
import matplotlib.pyplot as plt
from unum.units import *

t = sp.symbols('t', real=True)


r1 = 120
r2 = 665
r3 = 120

b = 2*sp.pi/100

vs = 2*sp.sin(2*t+0.4)+.9*sp.sin(3.5*t+.1)

Rp = (r2 * r3) / (r2 + r3)

# Total current
#iT = vs / (r1 + Rp)

v1 = vs/(125.4)

#iR2 = v1 / r2
#iR3 = v1 / r3

#i0 = iT - iR2 - iR3

print(f"Voltage v1: {v1}")


#Plot v1 over time
time = np.linspace(0, 50, 1000)
vs_func = sp.lambdify(t, vs, modules=['numpy', {'ohm': 1, 'V': 1}])
vs_values = vs_func(time)   
v1_func = sp.lambdify(t, v1, modules=['numpy', {'ohm': 1, 'V': 1}])
v1_values = v1_func(time)
plt.plot(time, v1_values*1000)
plt.plot(time, vs_values)
plt.title('Voltage v1 over time')
plt.xlabel('Time (us)')
plt.ylabel('Voltage v1 (V)') 
plt.grid()
plt.show()   

