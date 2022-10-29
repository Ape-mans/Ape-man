import numpy as np
from LengthCounter import LengthCounter


class GradientDescent:
    """Class was made to implement Gradient Descent method of function minimization"""
    def __init__(self, func, step):
        """
        Constructor of Gradient Descent method

            func: function(point: (float, float)) : float

            Chooser of the next step:
                step: Step Chooser Instance
        """
        self.func = func
        self.step = step

    def do(self, e, start_point):
        """
        Calling method function from class instance

            Accuracy error:
                e: float

            Start point:
                start_point: (float, float)

        Return:
            count of iteration, end point, list of between points
        """
        return GradientDescent.do_descent(self.func, self.step, e, start_point)

    @staticmethod
    def do_descent(func, step, e, start_point):
        """
        Static calling of descent function

            func: function(point: (float, float)) : float

            Chooser of the next step:
                step: Step Chooser Instance

            Accuracy error:
                e: float

            Start point:
                start_point: (float, float)

        Return:
            count of iteration, end point, list of between points
        """
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
        """
        Func to get gradient for current point

            func: function(point: (float, float)) : float


            Current point:
                point: (float, float)

            Accuracy error:
                e: float

        Return:
            gradient: (float, float)
        """
        return np.array([(func([point[j] + e if j == i else point[j] for j in range(len(point))]) - func(point)) / e
                         for i in range(len(point))])
