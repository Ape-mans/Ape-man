import math


class Parabolic:
    def __init__(self, func):
        self._func = func


    @staticmethod
    def _top_of_parabola(m, l, r, fm, fl, fr):
        denominator = 2 * ((m - l) * (fm - fr) - (m - r) * (fm - fl))
        if denominator == 0:
            return None
        return m - ((fm - fr) * (m - l) ** 2 - (fm - fl) * (m - r) ** 2) / denominator


    @staticmethod
    def do_method(func, left, right, e):
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
        return Parabolic.do_method(self._func, left, right, e)




