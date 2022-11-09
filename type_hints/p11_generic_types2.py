from typing import TypeVar


T = TypeVar("T", int, float, str)
K = TypeVar("K", int, float, str)


def test(x: T) -> T:
    print(x)  # 888
    print(type(x))  # <class 'int'>
    return x


test(888)
