import math


class GoldenRatio:
    """Class was made to implement Golden Ratio method of function minimization"""
    def __init__(self, func):
        """
        Constructor of Golden Ratio method

            func: function(x: float) : float
        """
        self._func = func

    @staticmethod
    def do_method(func, left, right, e):
        """
        Static calling of method function

            func: function(x: float) : float

            Accuracy error:
                e: float

            Search boundaries:
                left: float
                right: float

        Return:
            minimum point of function, count of iteration, distance between right and left border
        """
        i = 0
        phi = (1 + 5**0.5) / 2
        resphi = 2 - phi
        x1 = left + resphi * (right - left)
        x2 = right - resphi * (right - left)
        f1 = func(x1)
        f2 = func(x2)
        while abs(right - left) > e:
            i += 1
            if (f1 < f2) > 0:
                right = x2
                x2 = x1
                x1 = left + resphi * (right - left)
                f2 = f1
                f1 = func(x1)
            else:
                left = x1
                x1 = x2
                x2 = right - resphi * (right - left)
                f1 = f2
                f2 = func(x2)
        return (x1 + x2) / 2, i, right - left

    def do(self, left, right, e):
        """
        Calling method function from class instance

            Accuracy error:
                e: float

            Search boundaries:
                left: float
                right: float

        Return:
            minimum point of function, count of iteration, distance between right and left border
        """
        return GoldenRatio.do_method(self._func, left, right, e)



