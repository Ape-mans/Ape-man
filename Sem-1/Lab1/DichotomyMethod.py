import math
import matplotlib.pyplot as plt


class Dichotomy:
    """Class was made to implement Dichotomy method of function minimization"""
    def __init__(self, func):
        """
        Constructor of Dichotomy method

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
        while abs(right - left) > e:
            i += 1
            middle = (right + left) / 2
            fml = func(middle - e / 2)
            fmr = func(middle + e / 2)
            if (fml < fmr) > 0:
                right = middle
            else:
                left = middle
        return (left + right) / 2, i, right - left

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
        return Dichotomy.do_method(self._func, left, right, e)





