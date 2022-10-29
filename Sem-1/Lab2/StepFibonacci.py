from Lab1.FibonacciMethod import Fibonacci


class StepFibonacci:
    """Class was made to implement making Fibonacci Step Chooser variant"""
    def __init__(self, step):
        """
        Constructor of next step chooser

        start step:
            step: float
        """
        self.step = step

    def get_step(self, func, point, grad, e):
        """
        Func to get next step

            func: function(point: (float, float)) : float

            Current point:
                point: (float, float)

            Current gradient:
                grad: (float, float)

            Accuracy error:
                e: float

        Return:
            next step
        """
        step = Fibonacci.do_method(lambda step: func(point - step * grad), 0, self.step, e)[0]
        return step

