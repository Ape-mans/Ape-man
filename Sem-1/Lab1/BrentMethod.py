import math


class Brent:
    """Class was made to implement Brent method of function minimization"""
    def __init__(self, func):
        """
        Constructor of Brent method

            func: function(x: float) : float
        """
        self._func = func

    @staticmethod
    def _top_of_parabola(x, w, v, fx, fw, fv):
        """
        Finding top of parabola

            variables:
                x: float
                w: float
                v: float

            func value to exact variable:
                fx: float
                fw: float
                fv: float

        Return:
            vertex of parabola from 3 points
        """
        denominator = 2 * ((w - x) * (fw - fv) - (w - v) * (fw - fx))
        if denominator == 0:
            return None
        return w - ((fw - fv) * (w - x) ** 2 - (fw - fx) * (w - v) ** 2) / denominator

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
        r = (3 - 5 ** 0.5) / 2
        x = w = v = left + r * (right - left)
        fx = func(x)
        fv = fx
        fw = fx
        d_cur = d_prv = right - left
        i = 0
        while right - left > e:
            i += 1
            if max(x - left, right - x) < e:
                break
            g = d_prv / 2
            d_prv = d_cur
            u = Brent._top_of_parabola(x, w, v, fx, fw, fv)
            if u is None or abs(u - x) > g/2 or u < left or u > right:
                if x < (left + right) / 2:
                    u = x + r * (right - x)
                    d_prv = right - x
                else:
                    u = x - r * (x - left)
                    d_prv = x - left
            fu = func(u)
            d_cur = abs(u - x)
            if fu > fx:
                if u < x:
                    left = u
                else:
                    right = u
                if fu <= fw or w == x:
                    v = w
                    fv = fw
                    w = u
                    fw = fu
                else:
                    if fu <= fw or v == x or v == w:
                        v = u
                        fv = fu
            else:
                if u < x:
                    right = x
                else:
                    left = x
                v = w
                fv = fw
                w = x
                fw = fx
                x = u
                fx = fu
        return x, i, right - left

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
        return Brent.do_method(self._func, left, right, e)




