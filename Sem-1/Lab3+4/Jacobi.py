"""Jacobi's method for solving systems of linear algebraic equations"""


class Jacobi:

    """The order of solving SLOUGH by the Jacobi method is as follows:
    ● Reduction of the system of equations to a form in which
    some unknown value of the system is expressed on each line.
    ● Arbitrary choice of the null solution, as it can be taken
    a vector column of free terms.
    ● We substitute an arbitrary zero solution into the system
    of equations obtained by subparagraph 1.
    ● Implementation of additional iterations, for each of which
    the solution obtained at the previous stage is used"""
    @staticmethod
    def solve(matrix, values, accuracy=1e-3, maxCountOfIterations=1000):
        n = len(values)
        x = [1 for _ in range(n)]

        for i in range(maxCountOfIterations):
            x_prev = x.copy()

            for k in range(n):
                s = 0
                for j in range(n):
                    if j != k:
                        s += matrix[k][j] * x[j]
                x[k] = values[k] / matrix[k][k] - s / matrix[k][k]
            if Jacobi._isNeedToEnd(x_prev, x, accuracy):
                break

        return x

    """If the relation less than our accuracy then we found closest answer
    There is no need to proceed calculations"""

    @staticmethod
    def _isNeedToEnd(x_prev, x, accuracy):
        s1 = 0
        s2 = 0
        for i in range(len(x)):
            s1 += (x[i] - x_prev[i]) ** 2
            s2 += (x[i]) ** 2

        return (s1 / s2) ** 0.5 < accuracy
