import numpy as np

from Lab3.LUDecomposition import LUDecomposition
from Lab3.SolveLU import SolveLU


class ReversedMatrixByLU:
    @staticmethod
    def get_reversed(L, U):
        n = L.shape[0]
        reversedMatrix = np.zeros((n, n))
        y = np.zeros((n, n))
        e = ReversedMatrixByLU._get_identity_matrix(n)
        L1, U1 = LUDecomposition.decompose_to_LU(L)
        for i in range(n):
            y[0:, i] = SolveLU.solve_LU(L1, U1, e[0:, i])

        L2, U2 = LUDecomposition.decompose_to_LU(U)
        for i in range(n):
            reversedMatrix[0:, i] = SolveLU.solve_LU(L2, U2, y[0:, i])

        return np.matrix(reversedMatrix)

    @staticmethod
    def _get_identity_matrix(n):
        e = np.zeros((n, n))
        for i in range(n):
            e[i, i] = 1
        return e
