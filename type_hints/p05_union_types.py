from typing import Union

xxx: Union[int, str] = 3

xxx = "17"


def foo(x: Union[int, str]) -> Union[int, str]:
    return x


print(foo(3))
print(foo("3"))
