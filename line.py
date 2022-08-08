from __future__ import annotations

from abc import (
    ABC,
    abstractmethod
)
from typing import Union
from fractions import Fraction

from point import Point2D
from utils_math import *

class Line(ABC):

    def __init__(self, dimension: int):
        self.dimension = dimension


class Line2D(Line):
    """a line in a 2D plane have the formula: ax + by + c = 0"""

    def __init__(self, *args):
        super().__init__(2)

        if len(args) == 3:
            if (not isinstance(args[0], (int, float))) or \
               (not isinstance(args[1], (int, float))) or \
               (not isinstance(args[2], (int, float))):
                raise Exception("Line's parameters must be a number")
            self.a, self.b, self.c = self._normalize_parameters(args[0], args[1], args[2])
        elif len(args) == 2:
            if not isinstance(args[0], Point2D):
                raise Exception("First parameter should be a point")
            if not isinstance(args[1], (int, float, Point2D)):
                raise Exception("Second parameter should be a number or a point")
            if isinstance(args[1], Point2D):
                point1, point2 = args[0], args[1]
                a = point2.y_coordinate - point1.y_coordinate
                b = point1.x_coordinate - point2.x_coordinate
                c = a * point1.x_coordinate + b * point1.y_coordinate
                self.a, self.b, self.c = self._normalize_parameters(a, b, c)
            if isinstance(args[1], (int, float)):
                """
                Equation with one point and slope is
                y - b = m(x - a) with point is (a, b)
                """
                a = -args[1]
                b = 1
                c = args[1] * args[0].x_coordinate - args[0].y_coordinate
                self.a, self.b, self.c = self._normalize_parameters(a, b, c)
        else:
            raise Exception("Invalid input's length")

    def __repr__(self):
        return f"Line({self.a}, {self.b}, {self.c})"


    @staticmethod
    def _normalize_parameters(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> \
        (int, int, int):
        a, b, c = round(a, 2), round(b, 2), round(c, 2)
        a_normalized, b_normalized, c_normalized = a, b, c

        if a <= b and a <= c:
            b_normalized, c_normalized, a_normalized = normalize_ratio_three(b, c, a)

        if b <= a and b <= c:
            a_normalized, c_normalized, b_normalized = normalize_ratio_three(a, c, b)

        if c <= a and c <= b:
            a_normalized, b_normalized, c_normalized = normalize_ratio_three(a, b, c)

        return a_normalized, b_normalized, c_normalized


if __name__ == '__main__':
    print(Line2D._normalize_parameters(1, 2, 0.5))
    print(Line2D._normalize_parameters(0.5, 1, 2))
    print(Line2D._normalize_parameters(1, 0.5, 2))