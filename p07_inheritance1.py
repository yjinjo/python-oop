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
        print("yes!")

    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call")
        print(f"{self.name} call!!")


class Siri(Robot):
    pass


siri = Siri("iPhone14 Pro")
print(siri)  # iPhone14 Pro robot!!

siri.are_you_robot()  # yes!

print(siri.cal_add(17, 19))  # 36
