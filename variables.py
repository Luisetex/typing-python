from typing import List, Tuple


x: int = 1
y: int = 3
z: str = 'Hello world'

simple_list: list = [1,2,3]
awesome_list: List[int] = [1,2,3]
simple_tuple: tuple = (1, 2, 3)
awesome_tuple: Tuple[int, int, int] = (1, 2, 3)

print(x + y)
# print(y + z)


reveal_type(x)
reveal_type(y)
reveal_type(z)
reveal_type(simple_list)
reveal_type(awesome_list)
reveal_type(simple_tuple)
reveal_type(awesome_tuple)

