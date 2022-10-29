import math


class Fibonacci:
    def __init__(self, func):
        self._func = func

    @staticmethod
    def _get_fibonacci_list(left, right, e):
        a = [1, 1]
        b = (right - left) / e
        while a[-1] < b:
            a.append(a[-1] + a[-2])
        return a

    @staticmethod
    def _last_part(func, left, right, e, x1, f1, n):
        x2 = x1 + e
        f2 = func(x2)
        if f1 - e < f2 < f1 + e:
            return (x1 + right) / 2, n, right - x1
        else:
            return (left + x2) / 2, n, x2 - left

    @staticmethod
    def do_method(func, left, right, e):
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
        return Fibonacci.do_method(self._func, left, right, e)



