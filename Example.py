import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from unum.units import *

# Define symbols
x, y = sp.symbols('x y')
t = sp.symbols('t', real=True)


r1 = 120 * ohm
r2 = 665 * ohm
r3 = 120 * ohm

vs = 5 * V

Rp = (r2 * r3) / (r2 + r3)

iT = vs / (r1 + Rp)

print(f"Current i: {iT}")









