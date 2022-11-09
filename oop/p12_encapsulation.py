class Robot:
    __population = 0

    def __init__(self, name, age):
        self.name = name
        self._age = age
        Robot.population += 1

    def __say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots.")


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(self.name)
        print(self._age)
        self._age = 999


ss = Robot("yss", 8)

ssss = Siri("iPhone 14 Pro", 9)
print(ssss._age)
