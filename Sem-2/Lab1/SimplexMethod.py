class SimplexMethod:

    @staticmethod
    def simplex(c, A, b):
        tableau = SimplexMethod.to_tableau(c, A, b)
        return tableau

    @staticmethod
    def to_tableau(c, A, b):
        xb = [eq + [x] for eq, x in zip(A, b)]
        z = c + [0]
        return xb + [z]

