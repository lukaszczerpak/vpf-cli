from vpfq.model.AbstractModel import AbstractModel
import numpy as np
from scipy.interpolate import interp1d


class LinearInterpolation(AbstractModel):
    @staticmethod
    def generate_values(ix, iy, segments, base_prob):
        k = segments / ix[-1]
        l = base_prob / 100
        f = interp1d([k * x for x in ix], [l * y for y in iy])
        xnew = np.arange(0, segments + 1).tolist()
        return zip(xnew, f(xnew))
