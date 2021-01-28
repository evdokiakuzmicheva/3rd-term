import numpy as np
from scipy import linalg

from sympy import symbols, Matrix, Eq, solve

#l0 - lambda
mu, l, ro, l0 = symbols('mu l ro l0')
A = np.array([[mu] * 9] * 9)
A -= A
A[3][0] = -(l + 2*mu)
A[6][0], A[8][0] = -l, -l
A[4][1], A[5][2] = -mu, -mu
A[0][3], A[1][4], A[2][5] = - 1 / ro, - 1 / ro, - 1 / ro
E = np.eye(9)
B = A - l0 * E
B = Matrix(B)
e = Eq(B.det(), 0)
print(solve(e, l0))
