class Jacobi:
    @staticmethod
    def solve(matrix, values, accuracy = 1e-3, maxCountOfIterations = 1000):
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

    @staticmethod
    def _isNeedToEnd(x_prev, x, accuracy):
        s1 = 0
        s2 = 0
        for i in range(len(x)):
            s1 += (x[i] - x_prev[i]) ** 2
            s2 += (x[i]) ** 2

        return (s1 / s2) ** 0.5 < accuracy
