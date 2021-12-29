from typing import List


class Datapoint:

    def __init__(self, value: float, position: List[float]):
        self.value = value
        self.position = position