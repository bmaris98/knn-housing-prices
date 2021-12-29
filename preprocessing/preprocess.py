import os

file_path = os.path.join(os.path.dirname(__file__), '../data/original.csv')
print(file_path)
target_data = []
with open(file_path, 'r') as fin:
    for index, line in enumerate(fin):
        splitted = line.replace('\n', '').replace('"', '').split(',')
        target_columns = splitted[2:16]
        target_columns.extend(splitted[19:])
        if not index == 0:
            target_columns = list(map(lambda x: float(x), target_columns))
        target_data.append(target_columns)

target_data = target_data
test_data_count = 1000
headers = target_data[0]
test_data = []
test_data.append(headers)
test_data.extend(target_data[len(target_data)-test_data_count:-1])
train_data = []
train_data.extend(target_data[0:len(target_data)-test_data_count])

def stringify(iter):
    data = [','.join([str(y) for y in x]) for x in iter]
    return '\n'.join(data)

test_data = stringify(test_data)
train_data = stringify(train_data)

def write_data(iter, name):
    file_path = os.path.join(os.path.dirname(__file__), '../data/' + name)
    with open(file_path, 'w') as fout:
        fout.writelines(iter)

write_data(test_data, 'test.csv')
write_data(train_data, 'train.csv')

