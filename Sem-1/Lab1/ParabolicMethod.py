import math


class Parabolic:
    """Class was made to implement Parabolic method of function minimization"""
    def __init__(self, func):
        """
        Constructor of Parabolic method

            func: function(x: float) : float
        """
        self._func = func


    @staticmethod
    def _top_of_parabola(m, l, r, fm, fl, fr):
        """
        Finding top of parabola

            variables:
                m: float
                l: float
                r: float

            func value to exact variable:
                fm: float
                fl: float
                fr: float

        Return:
            vertex of parabola from 3 points
        """
        denominator = 2 * ((m - l) * (fm - fr) - (m - r) * (fm - fl))
        if denominator == 0:
            return None
        return m - ((fm - fr) * (m - l) ** 2 - (fm - fl) * (m - r) ** 2) / denominator


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
        middle = (left + right) / 2
        fl = func(left)
        fm = func(middle)
        fr = func(right)
        while fm < fl and fm < fr and right - left > e:
            i += 1
            u = Parabolic._top_of_parabola(middle, left, right, fm, fl, fr)
            fu = func(u)
            if fu <= fm:
                if u < middle:
                    right = middle
                    fr = fm
                else:
                    left = middle
                    fl = fm
                middle = u
                fm = fu
            else:
                if u < middle:
                    left = u
                    fl = fu
                else:
                    right = u
                    fr = fu
            if i > 1 and abs(xi - u) < e:
                break
            xi = u
        return u, i, right - left

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
        return Parabolic.do_method(self._func, left, right, e)




