from abc import ABC, abstractmethod
import os

class Writer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def write(self, string: str) -> None:
        raise NotImplementedError


class FileWriter(Writer):
    def __init__(self, filename):
        self.file_path = os.path.join(os.path.dirname(__file__), '../data/' + filename)
        with open(self.file_path, 'w'):
            pass

    def write(self, string: str) -> None:
        with open(self.file_path, 'a') as fout:
            fout.write(string + '\n')

class ConsoleWriter(Writer):
    def __init__(self):
        pass

    def write(self, string: str) -> None:
        print(string)