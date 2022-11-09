from typing import TypeVar, Generic


T = TypeVar("T", int, float, str)
K = TypeVar("K", int, float, str)


class Robot(Generic[T, K]):
    def __init__(self, arm: T, head: K):
        self.arm = arm
        self.head = head

    def decode(self):
        # 암호를 해독하는 코드 (복잡)
        pass


robot1 = Robot[int, int](123124, 134256234)
robot2 = Robot[str, int]("234234", 235346345)
robot3 = Robot[float, str](325.236, "333745684")


class Siri(Generic[T, K], Robot[T, K]):
    pass


siri1 = Siri[int, int](123124, 134256234)
siri2 = Siri[str, int]("234234", 235346345)
siri3 = Siri[float, str](325.236, "333745684")

print(siri1.arm)
