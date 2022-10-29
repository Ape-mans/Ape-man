import numpy as np
from LengthCounter import LengthCounter


class GradientDescent:
    def __init__(self, func, step):
        self.func = func
        self.step = step

    def do(self, e, start_point):
        return GradientDescent.do_descent(self.func, self.step, e, start_point)

    @staticmethod
    def do_descent(func, step, e, start_point):
        iteration = 0
        points = []
        point = np.array(start_point)
        points.append(point.copy())
        grad = GradientDescent._gradient(func, point, e)
        lam = step.get_step(func, point, grad, e)
        while LengthCounter.get(lam * grad) > e:
            iteration += 1
            point -= lam * grad
            points.append(point.copy())
            grad = GradientDescent._gradient(func, point, e)
            lam = step.get_step(func, point, grad, e)
        return iteration, point, points

    @staticmethod
    def _gradient(func, point, e):
        return np.array([(func([point[j] + e if j == i else point[j] for j in range(len(point))]) - func(point)) / e
                         for i in range(len(point))])
