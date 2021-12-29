import math
from typing import List


class Normalizer:

    def __init__(self):
        self._maxes: List[float] = []

    def load(self, data: List[List[float]]) -> None:
        columns_count: int = len(data[0])
        self._maxes = [float(-math.inf)] * columns_count
        for entry in data:
            for index, value in enumerate(entry):
                if self._maxes[index] < abs(value):
                    self._maxes[index] = abs(value)
        
    def normalize(self, entry: List[float]) -> List[float]:
        normalized_entry: List[float] = []
        for index, value in enumerate(entry):
            normalized_value = value / self._maxes[index]
            normalized_entry.append(normalized_value)
            
        return normalized_entry
