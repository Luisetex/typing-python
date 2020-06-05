from typing import List


class Point:
    def __init__(self, pos_x: int, pos_y: int, pos_z: int, name: str) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.name = name

    def print_position(self) -> None:
        print(self.pos_x, self.pos_y, self.pos_z)

Points = List[Point]

def print_points(points: Points) -> None:
    for point in points:
        print(point.name)
        point.print_position()

point_a = Point(0, 0, 0, 'a')
point_b = Point(1, 2, 3, 'b')
point_c = Point(4, -21, 9, 'c')


point_list = [point_a, point_b, point_c]
print_points(point_list)


reveal_type(point_a)
reveal_type(point_list)
