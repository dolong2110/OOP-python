from abc import (
    ABC,
    abstractmethod
)

class Point(ABC):

    def __init__(self, dimension: int):
        self.dimension = dimension

    @abstractmethod
    def get_distance(self, point, metric: str) -> [int, float]:
        pass

    @abstractmethod
    def get_symmetrical_point(self):
        pass


class Point2D(Point):

    def __init__(self, x_coordinate: [int, float], y_coordinate: [int, float]):
        super().__init__(2)
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def __repr__(self):
        return f"Point({self.x_coordinate}, {self.y_coordinate})"


    def get_distance(self, point, metric: str) -> [int, float]:
        if metric == 'L1':
            return abs(self.x_coordinate - point.x_coordinate) + \
                   abs(self.y_coordinate - point.y_coordinate)

        if metric == 'L2':
            return ((self.x_coordinate - point.x_coordinate) ** 2 +
                    (self.y_coordinate - point.y_coordinate) ** 2) ** 0.5

        return 0

    def get_symmetrical_point(self):
        return self.__class__(-self.x_coordinate, -self.y_coordinate)


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
