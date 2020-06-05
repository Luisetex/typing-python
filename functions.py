from typing import Callable, TypeVar

def sum(num_a: int, num_b: int) -> int:
    return num_a + num_b

result_sum = sum(5, 10)

# bad_result = sum(27, 29.04)

def subtract(num_a: int, num_b: int) -> int:
    return num_a - num_b

T = TypeVar('T', 'int', 'float')

def print_compute(computation: Callable[[int, int], int], num_a: T, num_b: T) -> None:
    print(computation(num_a, num_b))


def multiply(num_a: T, num_b: T) -> T:
    return num_a * num_b

# Good Result
print_compute(multiply, 10, 314)