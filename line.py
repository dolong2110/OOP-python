from abc import (
    ABC,
    abstractmethod
)
from typing import Union

class Line(ABC):

    def __init__(self, dimension: int):
        self.dimension = dimension


class Line2D(Line):

    def __init__(self, *args):
        super().__init__(2)
