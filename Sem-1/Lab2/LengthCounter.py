class LengthCounter:
    @staticmethod
    def get(vector):
        return sum([i ** 2 for i in vector]) ** 0.5

    @staticmethod
    def get_norm(vector):
        return sum([i ** 2 for i in vector])
