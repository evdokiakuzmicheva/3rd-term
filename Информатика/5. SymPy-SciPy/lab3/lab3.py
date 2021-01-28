# dy(x)
# ----- = -2y(x), y(0) = sqrt(2)
# dx
from scipy.integrate import odeint
import os
from sys import exit
import numpy as np
from scipy import linalg
from matplotlib import pyplot as plt
from sympy import symbols, Matrix, Eq, solve, integrate

x, y, C = symbols('x y C')
e = Eq(integrate(1 / y, y), -2*x)
sol = solve(e, y)[0]
e = Eq(sol.evalf(subs={x: 0}) + C, np.sqrt(2))
C = solve(e, C)[0]
sol += C
fig, ax = plt.subplots(1, 2)
dx = 0.1
X = np.linspace(start = -10, stop = 0, num = int(20 / dx))
Y = []
for i in range(len(X)):
    Y.append(sol.evalf(subs = {x: X[i]}))
ax[0].plot(X, Y)
ax[0].set_title('SymPy', fontfamily = 'fantasy')

def dydt(y, t):
    return -2*y

t = np.linspace( -10, 0, 200)
y0 = np.e **(-2*(-10)) # start value
y = odeint (dydt, y0, t) # solve eq.
C = y[len(y) - 1] - np.sqrt(2)
y = np.array(y).flatten() + C
plt.plot(t, y)
ax[1].set_title('SciPy', fontfamily = 'fantasy')

for _ in ax:
    _.grid()
    _.set_xlabel('x')
    _.set_ylabel('y')

plt.show()
