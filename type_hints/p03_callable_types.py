from typing import Callable


def add(a: int, b: int) -> int:
    return a + b


def test():
    pass


def foo(func: Callable[[int, int], int]) -> int:
    return func(2, 3)


print(foo(add))
# print(foo(test))  # Error
