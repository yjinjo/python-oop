class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots.")


class Siri(Robot):
    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        return a * b


siri = Siri("iPhone 14 Pro")

print(Siri.mro())  # [<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]

print(Robot.mro())  # [<class '__main__.Robot'>, <class 'object'>]

print(dir(object))
print(object.__name__)

print(int.mro())


class A:
    pass


class B:
    pass


class C:
    pass


class D(A, B, C):
    pass


print(
    D.mro()
)  # [<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
