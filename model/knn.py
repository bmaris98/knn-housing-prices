from math import dist
from typing import List, Tuple
from model.datapoint import Datapoint
from model.distance import Distance
from model.normalizer import Normalizer


class KNN:
    def __init__(self, k: int, data: List[Datapoint], distance: Distance, normalizer: Normalizer):
        self._data: List[Datapoint] = data
        self._k: int = k
        self._normalizer: Normalizer = normalizer
        self._distance: Distance = distance
        self._normalize_data()

    def _normalize_data(self) -> None:
        self._data = [Datapoint(x.value, self._normalizer.normalize(x.position)) for x in self._data]

    def predict(self, entry: List[float]) -> float:
        scores: List[Tuple[Datapoint, float]] = []
        entry = self._normalizer.normalize(entry)
        # scores = list(map(lambda x: (x, self._distance.compute_distance(x.position, entry)), self._data))
        # scores = [(x, self._distance.compute_distance(x.position, entry)) for x in self._data]
        for datapoint in self._data:
            distance = self._distance.compute_distance(datapoint.position, entry)
            scores.append((datapoint, distance))
        
        scores.sort(key=lambda x: x[1])
        first_k = scores[0:self._k]
        sum: float = 0.0
        for neighbor in first_k:
            sum += neighbor[0].value
        return sum/self._k
