import numpy as np

from Lab3.LUDecomposition import LUDecomposition
from Lab3.SolveLU import SolveLU


class HilbertSolution:
    @staticmethod
    def solve_LU(n):
        A = np.random.randint(10, size=(n, n))
        print(A)
        L, U = LUDecomposition.decompose_to_LU(A)
        b = np.random.randint(10, size=(n, 1))
        print(b)
        return SolveLU.solve_LU(L, U, b)

    @staticmethod
    def hilbert(n):
        return [[1 / (i + j + 1) for j in range(n)] for i in range(n)]
