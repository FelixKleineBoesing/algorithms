from algorithms._apsp import apsp
import numpy as np


def pyapsp(dist: np.ndarray):
    apsp(dist, dist.shape[0])