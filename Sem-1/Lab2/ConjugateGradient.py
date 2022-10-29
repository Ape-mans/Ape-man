from LengthCounter import LengthCounter
import numpy as np


class ConjugateGradient:
    def __init__(self, func, step):
        self.func = func
        self.step = step

    def do(self, e, start_point):
        return ConjugateGradient.do_descent(self.func, self.step, e, start_point)

    @staticmethod
    def do_descent(func, step, e, start_point):
        iteration = 0
        points = []
        point = np.array(start_point)
        p_pr = np.array(ConjugateGradient._gradient(func, point, e))
        grad_pr = np.array([0., 0.])
        f = func(point)
        f_next = f
        while iteration == 0 \
                or ((LengthCounter.get(point) - LengthCounter.get(next_point)) / LengthCounter.get(point) > e
                    or abs(f_next - f) > e):
            points.append(point.copy())
            if LengthCounter.get_norm(grad_pr) == 0 or (iteration + 1) % 3 == 0:
                beta = 0
                p_pr = -ConjugateGradient._gradient(func, point, e)
            else:
                beta = LengthCounter.get_norm(grad) / LengthCounter.get_norm(grad_pr)
            iteration += 1
            grad = ConjugateGradient._gradient(func, point, e)
            lamb = step.get_step(func, point, grad, e)
            next_point = point + lamb * p_pr
            p = -ConjugateGradient._gradient(func, next_point, e) + beta * p_pr
            f = f_next
            f_next = func(next_point)
            point = next_point
            p_pr = p
            grad_pr = grad
            points.append(point)
        return iteration, point, points

    @staticmethod
    def _gradient(func, point, e):
        return np.array([(func([point[j] + e if j == i else point[j] for j in range(len(point))]) - func(point)) / e
                         for i in range(len(point))])
