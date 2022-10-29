import numpy as np

from Lab3.LUDecomposition import LUDecomposition
from Lab3.SolveLU import SolveLU

"""Create LU-decompostion from Hilbert Matrix and solve it
For more info check: LUDecomposition and SolveLU Files"""
class HilbertSolution:
    @staticmethod
    def solve_LU(n):
        A = np.random.randint(10, size=(n, n))
        print(A)
        L, U = LUDecomposition.decompose_to_LU(A)
        b = np.random.randint(10, size=(n, 1))
        print(b)
        return SolveLU.solve_LU(L, U, b)

    """In linear algebra, a Hilbert matrix, introduced by Hilbert (1894), is a square matrix with entries being the unit fractions
        H_{ij}={1} / {i+j-1}}"""
    @staticmethod
    def hilbert(n):
        return [[1 / (i + j + 1) for j in range(n)] for i in range(n)]
