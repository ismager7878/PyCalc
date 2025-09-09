import sympy as sp
from sympy import pprint

import numpy as np
import matplotlib.pyplot as plt
from unum.units import *


L = .5 * m

mass = 1 * kg

tau = 1*.2 * N * m

theta = 30


grav = 9.81 * m / s**2 * mass * 1/2

gravTau = (1*grav * L * np.sin(np.radians(theta))).asUnit(N*m)

totalTau = tau - gravTau 

I = (mass * L**2)/3

print(f"I: {I}")
print(f"Total Torque: {totalTau}")
print(f"Gravitational Torque: {gravTau}")

acc = totalTau / I

print(f"Angular Acceleration: {acc}")


