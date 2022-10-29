from Lab1.FibonacciMethod import Fibonacci


class StepFibonacci:
    def __init__(self, step):
        self.step = step

    def get_step(self, func, point, grad, e):
        step = Fibonacci.do_method(lambda step: func(point - step * grad), 0, self.step, e)[0]
        return step

