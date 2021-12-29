from abc import ABC, abstractmethod
from typing import List
from scipy import spatial
import math

class Distance(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def compute_distance(self, left: List[float], right: List[float]) -> float:
        raise NotImplementedError


class EuclideanDistance(Distance):
    def __init__(self):
        pass

    def compute_distance(self, left: List[float], right: List[float]) -> float:
        sum: float = 0.0
        for i in range(len(left)):
            sum += math.pow(left[i] - right[i], 2)
        return math.sqrt(sum)


class ManhattanDistance(Distance):

    def __init__(self):
        pass

    def compute_distance(self, left: List[float], right: List[float]) -> float:
        sum: float = 0.0
        for i in range(len(left)):
            sum += abs(left[i] - right[i])
        return sum

class CosineDistance(Distance):
    def __init__(self):
        pass

    def compute_distance(self, left: List[float], right: List[float]) -> float:
        return spatial.distance.cosine(left, right)

class MinkowskiDistance(Distance):
    def __init__(self):
        pass

    def compute_distance(self, left: List[float], right: List[float]) -> float:
        return spatial.distance.minkowski(left, right, 3)