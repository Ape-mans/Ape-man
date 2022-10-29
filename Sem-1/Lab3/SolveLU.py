import numpy as np


class SolveLU:
    @staticmethod
    def solve_LU(L, U, b):
        n = len(L)
        y = np.zeros(n)
        for i in range(n):
            y[i] = b[i] / L[i][i]
            for k in range(i):
                y[i] -= y[k] * L[i][k]

        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = y[i] / U[i][i]
            for k in range(i + 1, n):
                x[i] -= x[k] * U[i][k]

        return x
