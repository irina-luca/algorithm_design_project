import numpy as np


def distance_euclidean(x1, x2):
    return np.linalg.norm(x1 - x2)


def SHD_distance(x1, x2):
    shd_xor = np.bitwise_xor(np.uint64(x1), np.uint64(x2))
    shd_and = np.bitwise_and(np.uint64(x1), np.uint64(x2)) + 0.00000001
    return np.count_nonzero(shd_xor) / np.count_nonzero(shd_and)


def AND_distance(x1, x2):
    return 1 - (np.count_nonzero(np.bitwise_and(np.uint64(x1), np.uint64(x2))) / len(x1))
