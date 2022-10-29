class LengthCounter:
    """Class was made to get length of vector"""
    @staticmethod
    def get(vector):
        """
        Get length of vector

        vector: (float, ..., float)
        """
        return sum([i ** 2 for i in vector]) ** 0.5

    @staticmethod
    def get_norm(vector):
        """
        Get squared length of vector

        vector: (float, ..., float)
        """
        return sum([i ** 2 for i in vector])
