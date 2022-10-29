from LengthCounter import LengthCounter


class StepConst:
    """Class was made to implement making Constant Step Chooser variant"""
    def __init__(self, step):
        """
        Constructor of next step chooser

        start step:
            step: float
        """
        self._step = step

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
        while func(point) < func(point - self._step * grad) and LengthCounter.get(self._step * grad) > e:
            self._step /= 2
        return self._step
