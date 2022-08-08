from __future__ import annotations

import math
from typing import Union

import numpy as np

from point import Point2D


class Circle:

    def __init__(self, *args):

        if len(args) == 2:
            if not isinstance(args[0], Point2D):
                raise Exception("First parameter should be a point")

            if not isinstance(args[1], int) and not isinstance(args[1], float):
                raise Exception("Second parameter should be and integer of float")

            if args[1] <= 0:
                raise Exception("Radius of a circle must be a positive number")

            self.center = Point2D(Circle.reduce_number_form(args[0].x_coordinate),
                                  Circle.reduce_number_form(args[0].y_coordinate))
            self.radius = Circle.reduce_number_form(args[1])
        elif len(args) == 3:
            if isinstance(args[0], Point2D) and isinstance(args[1], Point2D) and isinstance(args[2], Point2D):
                center, radius = Circle.get_circle_from_three_points(args[0], args[1], args[2])
                if radius < 0:
                    raise Exception("Radius of a circle must be a positive number")
                self.center = center
                self.radius = radius
            elif isinstance(args[0], (int, float)) and \
                    isinstance(args[1], (int, float)) and \
                    isinstance(args[2], (int, float)):
                if args[2] <= 0:
                    raise Exception("Radius of a circle must be a positive number")

                self.center = Point2D(self.reduce_number_form(args[0]), self.reduce_number_form(args[1]))
                self.radius = self.reduce_number_form(args[2])
            else:
                raise Exception("Invalid initialize parameter")
        else:
            raise Exception("Invalid initialize parameters")

    def __repr__(self):
        return f"Circle({self.center}, {self.radius})"

    def get_diameter(self) -> float:
        return round(2 * math.pi * self.radius, 6)

    def get_area(self) -> float:
        return round(math.pi * self.radius ** 2)

    def get_point_relation(self, point: Point2D) -> str:
        distance = point.get_distance(self.center, "L2")
        if distance < self.radius:
            return f"{point} lines inside the circle"
        if distance == self.radius:
            return f"{point} lines in circle's circumference"

        return f"{point} lines outside the circle"

    def get_circle_relation(self, circle: Circle) -> str:
        radius_distance = circle.center.get_distance(self.center, "L2")
        total_distance = self.radius + circle.radius
        if radius_distance == 0:
            return "Two circle are concentric to each other"
        if radius_distance < abs(self.radius - circle.radius):
            return "Two circle are containing each other"
        if radius_distance == abs(self.radius - circle.radius):
            return "Two circle are internally tangent to each other"
        if radius_distance < total_distance:
            return "Two circle are intersect to each other"
        if radius_distance == total_distance:
            return "Two circle are externally tangent to each other"

        return "Two circle are not having any common to each other"

    @staticmethod
    def get_circle_from_three_points(point1: Point2D, point2: Point2D, point3: Point2D) -> (Point2D, Union[int, float]):
        """
        function to convert 3 points into a Circle instance
        circle equation: x^2 + y^2 - 2ax - 2by - c = 0
        Put all 3 points into above equation we get matrix:
        Ax = b
        """

        A = np.array([[2 * point1.x_coordinate, 2 * point1.y_coordinate, 1],
                      [2 * point2.x_coordinate, 2 * point2.y_coordinate, 1],
                      [2 * point3.x_coordinate, 3 * point1.y_coordinate, 1]])

        b = np.array([[point1.x_coordinate ** 2 + point1.y_coordinate ** 2],
                      [point2.x_coordinate ** 2 + point2.y_coordinate ** 2],
                      [point3.x_coordinate ** 2 + point3.y_coordinate ** 2]])

        result = np.linalg.solve(A, b)
        return Point2D(Circle.reduce_number_form(result[0][0]),
                       Circle.reduce_number_form(result[1][0])),  Circle.reduce_number_form(result[2][0])

    @staticmethod
    def reduce_number_form(num: Union[int, float]) -> Union[int, float]:
        if isinstance(num, int):
            return num

        if num.is_integer():
            return int(num)

        return num


# if __name__ == '__main__':
#     c1 = Circle(3, 5, 2)
#     c2 = Circle(Point2D(1, 2), 3)
#     c3 = Circle(Point2D(0, 0), Point2D(1, 1), Point2D(1, 0))
#     c4 = Circle(Point2D(0, 0), -1)
#     c5 = Circle(Point2D(1, 2), Point2D(5, 3), Point2D(-1, 2))
# #
#     print(c1)
#     print(c2)
#     print(c3)
#     print(c4)
#     print(c5)
#     c1 = Circle(0, 0, 2)
#     c2 = Circle(0, 1, 0.5)
#     c3 = Circle(0, 1.5, 0.5)
#     c4 = Circle(0, 0, 2)
#     c5 = Circle(0, 0, 1)
#     c6 = Circle(0, 3, 2)
#     c7 = Circle(0, 4, 2)
#     c8 = Circle(0, 5, 2)
#     print(c1.get_circle_relation(c2))
#     print(c1.get_circle_relation(c3))
#     print(c1.get_circle_relation(c4))
#     print(c1.get_circle_relation(c5))
#     print(c1.get_circle_relation(c6))
#     print(c1.get_circle_relation(c7))
#     print(c1.get_circle_relation(c8))
