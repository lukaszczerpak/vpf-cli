from abc import abstractmethod


class AbstractModel:
    @staticmethod
    @abstractmethod
    def generate_values(ix, iy, segments, base_prob):
        raise NotImplemented()
