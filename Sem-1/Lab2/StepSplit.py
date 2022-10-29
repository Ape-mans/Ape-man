from LengthCounter import LengthCounter


class StepSplit:
    """Class was made to implement making Split Step Chooser variant"""
    def __init__(self, step, gamma):
        """
        Constructor of next step chooser

        start step:
            step: float

        reducing gamma:
            gamma: float (0, 1)
        """

        self._step = step
        self._gamma = gamma

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
        step = self._step
        while func(point - step * grad) > func(point) - e * step * LengthCounter.get(grad) ** 2 and LengthCounter.get(step * grad) > e:
            step *= self._gamma
        return step
