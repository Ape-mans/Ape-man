from Lab1.GoldenRatioMethod import GoldenRatio


class StepGoldenRatio:
    def __init__(self, step):
        self.step = step

    def get_step(self, func, point, grad, e):
        step = GoldenRatio.do_method(lambda step: func(point - step * grad), 0, self.step, e)[0]
        return step
