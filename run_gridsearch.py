import os
from typing import List
from model.datapoint import Datapoint
from model.distance import CosineDistance, EuclideanDistance, ManhattanDistance, MinkowskiDistance
from model.gridsearch import GridSearch
from model.writer import FileWriter

# grid search for [distances], [ks], split_cross_validation

def read_data(filename: str) -> List[Datapoint]:
    file_path = os.path.join(os.path.dirname(__file__), 'data/' + filename)
    datapoints: List[Datapoint] = []
    with open(file_path, 'r') as fin:
        for index, line in enumerate(fin):
            if index == 0:
                continue
            splitted = line.replace('\n', '').replace('"', '').split(',')
            value = float(splitted[0])
            position = splitted[1:]
            position = [float(x) for x in position]
            datapoints.append(Datapoint(value, position))
    return datapoints

train_data = read_data('train.csv')
train_data = train_data[0:1000]
writer = FileWriter('gridsearch.txt')
gs = GridSearch(5, [MinkowskiDistance(), CosineDistance(), ManhattanDistance(), EuclideanDistance()], range(15, 20), train_data, writer)
res = gs.fit()