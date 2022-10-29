import math


class Fibonacci:
    """Class was made to implement Fibonacci method of function minimization"""
    def __init__(self, func):
        """
        Constructor of Fibonacci method

            func: function(x: float) : float
        """
        self._func = func

    @staticmethod
    def _get_fibonacci_list(left, right, e):
        """
        Creation fibonacci list from first to value that less than (right - left) / e

            Accuracy error:
                e: float

            Search boundaries:
                left: float
                right: float

        Return:
            list of fibonacci numbers
        """
        a = [1, 1]
        b = (right - left) / e
        while a[-1] < b:
            a.append(a[-1] + a[-2])
        return a

    @staticmethod
    def _last_part(func, left, right, e, x1, f1, n):
        """
        Creation fibonacci list from first to value that less than (right - left) / e

            func: function(x: float) : float

            variables:
                x1: float

            func value to exact variable:
                f1: float

            Accuracy error:
                e: float

            Search boundaries:
                left: float
                right: float

            Len of gotten fibonacci list:
                n: int

        Return:
            minimum point of function, count of iteration, distance between right and left border
        """
        x2 = x1 + e
        f2 = func(x2)
        if f1 - e < f2 < f1 + e:
            return (x1 + right) / 2, n, right - x1
        else:
            return (left + x2) / 2, n, x2 - left

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
        fibonacci_list = Fibonacci._get_fibonacci_list(left, right, e)
        n = len(fibonacci_list)
        x1 = left + (right - left) * fibonacci_list[-3] / fibonacci_list[-1]
        x2 = left + (right - left) * fibonacci_list[-2] / fibonacci_list[-1]
        f1 = func(x1)
        f2 = func(x2)
        for i in range(0, n):
            if f1 <= f2:
                right = x2
                x2 = x1
                x1 = left + (right - left) * fibonacci_list[-3 - i] / fibonacci_list[-1 - i]
                f2 = f1
                f1 = func(x1)
                if i == n - 3:
                    return Fibonacci._last_part(func, left, right, e, x1, f1, n)
            else:
                left = x1
                x1 = x2
                x2 = left + (right - left) * fibonacci_list[-2 - i] / fibonacci_list[-1 - i]
                f1 = f2
                f2 = func(x2)
                if i == n - 3:
                    return Fibonacci._last_part(func, left, right, e, x1, f1, n)

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
        return Fibonacci.do_method(self._func, left, right, e)



