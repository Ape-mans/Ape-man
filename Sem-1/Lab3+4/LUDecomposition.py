import numpy as np

"""LU-decomposition of matrix A"""


class LUDecomposition:
    @staticmethod
    def decompose_to_LU(A):
        n = len(A)
        """A lower triangular matrix with a unit diagonal"""
        L = np.zeros((n, n))

        """Upper triangular matrix"""
        U = [[A[i][j] for j in range(n)] for i in range(n)]

        """We bring the A|E matrix to a triangular or stepped form. We get
        the matrix U|L0, where U is the upper triangular or step matrix, and L0 is
        the lower triangular matrix. Note that the resulting
        matrix L0 leads A to a triangular or stepped form"""

        """Since L0 is a square non-degenerate matrix, therefore it has
        an inverse matrix = L"""
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
