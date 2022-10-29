import numpy as np


class LUDecomposition:
    @staticmethod
    def decompose_to_LU(A):
        n = len(A)
        L = np.zeros((n, n))
        U = [[A[i][j] for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                L[j][i] = U[j][i] / U[i][i]

        for k in range(1, n):

            for i in range(k - 1, n):
                for j in range(i, n):
                    L[j][i] = U[j][i] / U[i][i]

            for i in range(k, n):
                for j in range(k - 1, n):
                    U[i][j] -= L[i][k - 1] * U[k - 1][j]

        return L, U
