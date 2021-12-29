from typing import List, Tuple
from model.distance import Distance
from model.datapoint import Datapoint
from time import time

import math

from model.knn import KNN
from model.normalizer import Normalizer
from model.writer import Writer

class GridSearch:

    def __init__(self, cv: int, distances: List[Distance], ks: List[int], data: List[Datapoint], writer: Writer):
        self._cv = cv
        self._distances = distances
        self._ks = ks
        self._data = data
        self._break_index = math.floor(len(self._data) / self._cv)
        self._normalizer = Normalizer()
        positions = [x.position for x in self._data]
        self._normalizer.load(positions)
        self.writer = writer

    def fit(self) -> List[Tuple[Distance, int, float]]:
        results: List[Tuple[Distance, int, float]] = []
        for distance in self._distances:
            for k in self._ks:
                start = time()
                error = self._get_error_for_config(distance, k)
                end = time()
                self.writer.write('Distance: ' + str(distance.__class__) + ' - k: ' + str(k) + ' - ' + str(error) + ' time elapsed: ' + str(end-start))
                results.append((distance, k, error))
        return results
    
    def _get_error_for_config(self, distance: Distance, k: int) -> float:
        config_avg_error: float = 0.0
        for i in range(self._cv):
            start_pos = i * self._break_index
            end_pos = (i+1) * self._break_index
            test_data: List[Datapoint] = self._data[start_pos:end_pos]
            train_data: List[Datapoint] = self._data[0:start_pos]
            train_data.extend(self._data[end_pos:])
            knn = KNN(k, train_data, distance, self._normalizer)
            
            errors = []
            for j in range(len(test_data)):
                error = abs(knn.predict(test_data[j].position) - test_data[j].value) / test_data[j].value
                errors.append(error)
            cv_config_avg_error = (sum(errors)/len(test_data))
            config_avg_error += cv_config_avg_error
            average_expected = 0
            for t in test_data:
                average_expected += t.value
            average_expected /= len(test_data)
            self.writer.write('Distance: ' + str(distance.__class__) + ' - k: ' + str(k) + ' - CV ' + str(i+1) + '/' + str(self._cv) + ' - ' + str(cv_config_avg_error) + ' - For avg. expected ' + str(average_expected))
        return config_avg_error / self._cv
