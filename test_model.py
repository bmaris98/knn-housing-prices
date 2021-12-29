import os
from typing import List
from model.datapoint import Datapoint
from model.distance import  ManhattanDistance
from model.normalizer import Normalizer
from model.knn import KNN
from model.writer import FileWriter

test_data_file = 'test_results.txt'

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
writer = FileWriter(test_data_file)
normalizer = Normalizer()
positions = [x.position for x in train_data]
normalizer.load(positions)
knn = KNN(18, train_data, ManhattanDistance(), normalizer)

test_data = read_data('test.csv')

writer.write('expected,predicted')
for datapoint in test_data:
    prediction = knn.predict(datapoint.position)
    writer.write(str(datapoint.value) + ',' + str(prediction))
print(sum / len(test_data))
normalizer = Normalizer()