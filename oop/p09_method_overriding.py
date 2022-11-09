class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots.")

    @staticmethod
    def are_you_robot():
        print(f"Robot.population: {Robot.population}")
        print("yes!")

    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call")
        print(f"{self.name} call!!")


class Siri(Robot):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Siri.population += 1

    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        self.a = a
        return a * b

    @classmethod
    def hello_apple(cls):
        print(f"cls: {cls}")

    # 메서드 오버라이딩
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name} by apple.")

    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots by apple")


siri = Siri("iPhone 14 Pro", 17)
siri.say_hi()  # Greetings, my masters call me iPhone 14 Pro by apple.
Siri.how_many()  # We have 1 robots by apple
