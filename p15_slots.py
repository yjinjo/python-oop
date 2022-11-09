class WithoutSlotClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


wos = WithoutSlotClass("amamob", 12)
print(wos.__dict__)  # {'name': 'amamob', 'age': 12}

wos.__dict__["hello"] = "world"
print(wos.__dict__)  # {'name': 'amamob', 'age': 12, 'hello': 'world'}


class WithSlotClass:
    # 속성을 미리 선언 (__dict__로 관리하는 것이 아닌 __slots__ 을 통해 관리할 수 있도록 만듦)
    __slots__ = {"name", "age"}

    def __init__(self, name, age):
        self.name = name
        self.age = age


ws = WithSlotClass("amamov", 12)
print(ws.__slots__)


import timeit


# 메모리 사용량 비교
def repeat(obj):
    def inner():
        obj.name = "amamov"
        obj.age = 222
        del obj.name
        del obj.age

    return inner


no_slot_time = timeit.repeat(repeat(wos), number=999)
use_slot_time = timeit.repeat(repeat(ws), number=999)

print(f"not use slot: {min(no_slot_time)}")
print(f"use slot: {min(use_slot_time)}")
