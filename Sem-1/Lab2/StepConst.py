from LengthCounter import LengthCounter


class StepConst:
    def __init__(self, step):
        self._step = step

    def get_step(self, func, point, grad, e):
        while func(point) < func(point - self._step * grad) and LengthCounter.get(self._step * grad) > e:
            self._step /= 2
        return self._step
