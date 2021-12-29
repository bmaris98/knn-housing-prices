import os
import math
from typing import List, Tuple

test_data_file = 'test_results.txt'

def read_data(filename: str) -> Tuple[List[float], List[float]]:
    file_path = os.path.join(os.path.dirname(__file__), 'data/' + filename)
    expected: List[float] = []
    actual: List[float] = []
    with open(file_path, 'r') as fin:
        for index, line in enumerate(fin):
            if index == 0:
                continue
            splitted = line.replace('\n', '').replace('"', '').split(',')
            expected.append(float(splitted[0]))
            actual.append(float(splitted[1]))
    return expected, actual

expected, actual = read_data('test_results.txt')

def mean_absolute_errors(expected: List[float], actual: List[float]) -> float:
    sum = 0
    for i in range(len(expected)):
        sum += abs(expected[i] - actual[i])
    return sum/len(expected)

def mean_percentage_error(expected: List[float], actual: List[float]) -> float:
    mae = mean_absolute_errors(expected, actual)
    avg_expected = sum(expected) / len(expected)
    return mae/avg_expected

def root_mean_squared_error(expected: List[float], actual: List[float]) -> float:
    sum = 0
    for i in range(len(expected)):
        sum += (expected[i] - actual[i]) ** 2
    return math.sqrt(sum/len(expected))

def normalized_mean_squared_error(expected: List[float], actual: List[float]) -> float:
    rmse = root_mean_squared_error(expected, actual)
    mean_expected = sum(expected) / len(expected)
    return rmse / mean_expected

mean_absolute_err = mean_absolute_errors(expected, actual)
mean_percentage_err = mean_percentage_error(expected, actual)
root_mean_squared_err = root_mean_squared_error(expected, actual)
normalized_mean_squared_err = normalized_mean_squared_error(expected, actual)

print('Mean absolute error: ' + str(mean_absolute_err ))
print('Mean percentage error: ' + str(mean_percentage_err))
print('Root mean absolute error: ' + str(root_mean_squared_err))
print('Normalized root mean squared error: ' + str(normalized_mean_squared_err))