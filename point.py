from __future__ import annotations

from abc import (
    ABC,
    abstractmethod
)
from typing import Union


class Point(ABC):

    def __init__(self, dimension: int):
        self.dimension = dimension

    @abstractmethod
    def get_distance(self, point, metric: str) -> Union[int, float]:
        pass

    @abstractmethod
    def get_symmetrical_point(self):
        pass


class Point2D(Point):

    def __init__(self, x_coordinate: Union[int, float], y_coordinate: Union[int, float]):
        super().__init__(2)
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def __repr__(self):
        return f"Point({self.x_coordinate}, {self.y_coordinate})"

    def __abs__(self, metric: str) -> Union[int, float]:
        """Returns the distance between this point and the origin."""
        return self.get_distance(self.__class__(0, 0), metric)

    def __add__(self, point: Point2D) -> Point2D:
        return self.__class__(self.x_coordinate + point.x_coordinate,
                              self.y_coordinate + point.y_coordinate)

    def __sub__(self, point: Point2D) -> Point2D:
        return self.__class__(self.x_coordinate - point.x_coordinate,
                              self.y_coordinate - point.y_coordinate)

    def __mul__(self, multiplier: Union[int, float]) -> Point2D:
        return self.__class__(self.x_coordinate * multiplier, self.y_coordinate * multiplier)

    def get_distance(self, point, metric: str, p: int = 1) -> Union[int, float]:
        """
        Return the distance with another point depends on the metric
        p here is used to calculate Minkowski distance
        """

        # Manhattan distance
        if metric == 'L1':
            return abs(self.x_coordinate - point.x_coordinate) + \
                   abs(self.y_coordinate - point.y_coordinate)

        # Euclidean distance
        if metric == 'L2':
            return ((self.x_coordinate - point.x_coordinate) ** 2 +
                    (self.y_coordinate - point.y_coordinate) ** 2) ** 0.5

        # Canberra distance
        if metric == 'L3':
            return abs(self.x_coordinate - point.x_coordinate) / (abs(self.x_coordinate) + abs(point.x_coordinate)) + \
                   abs(self.y_coordinate - point.y_coordinate) / (abs(self.y_coordinate) + abs(point.y_coordinate))

        # Hamming distance
        if metric == 'L4':
            return (abs(self.x_coordinate - point.x_coordinate) + abs(self.y_coordinate - point.y_coordinate)) / 2

        # Minkowski distance
        if metric == 'L5':
            return ((abs(self.x_coordinate - point.x_coordinate) ** p +
                     abs(self.y_coordinate - point.y_coordinate)) ** p) ** (1 / p)

        return 0

    def get_symmetrical_point(self):
        return self.__class__(-self.x_coordinate, -self.y_coordinate)

    def get_slope_from_origin(self) -> float:
        if self.x_coordinate == 0:
            return 0.0

        return self.y_coordinate / self.x_coordinate

    def dot(self, point: Point2D) -> Union[int, float]:
        """Return dot product of self with another Point"""

        return self.x_coordinate * point.x_coordinate + self.y_coordinate * point.y_coordinate

    def equal(self, point: Point2D) -> bool:
        """Returns whether the coordinates of self and other agree"""

        return (self.x_coordinate == point.x_coordinate) and (self.y_coordinate == point.y_coordinate)



# class Point3D(Point):
#
#     def __init__(self, x_coordinate: [int, float], y_coordinate: [int, float], z_coordinate: [int, float]):
#         super().__init__(3)
#         self.x_coordinate = x_coordinate
#         self.y_coordinate = y_coordinate
#         self.z_coordinate = z_coordinate
#
#     def get_coordinate(self) -> str:
#         return f"(The coordinate of the point is: " \
#                f"{self.x_coordinate}, {self.y_coordinate}, {self.z_coordinate})"
