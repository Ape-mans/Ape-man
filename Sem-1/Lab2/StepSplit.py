from LengthCounter import LengthCounter


class StepSplit:
    def __init__(self, step, gamma):
        self._step = step
        self._gamma = gamma

    def get_step(self, func, point, grad, e):
        step = self._step
        while func(point - step * grad) > func(point) - e * step * LengthCounter.get(grad) ** 2 and LengthCounter.get(step * grad) > e:
            step *= self._gamma
        return step
