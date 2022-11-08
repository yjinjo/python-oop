class Robot:
    """
    [Robot Class]
    Author: Youngjin Jo
    Role: ???

    Returns:
        _type_: _description_
    """

    # 클래스 변수: 각각의 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수: 인스턴스가 생성될 때 초기화시켜주는 함수
    def __init__(self, name):
        self.name = name  # 인스턴스 변수
        # 인스턴스를 찍어낼 때마다 각각의 인스턴스들이 공유하는 변수의 값을 1 증가시킴
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        # NLP Code ...
        print(f"Greetings, my masters call me {self.name}.")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    # 인스턴스 메서드
    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        """인스턴스 메서드의 self는 인스턴스를 받았다면, 클래스 메서드의 cls는 클래스를 받는다."""
        print(f"We have {cls.population} robots.")

    @staticmethod
    def are_you_robot():
        print("yes!")

    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call")
        print(f"{self.name} call!!")


droid1 = Robot("R2-D2")
droid1.say_hi()  # Greetings, my masters call me R2-D2.

# print(dir(droid1))

print(droid1)  # <__main__.Robot object at 0x1066f0550>
print(droid1.__str__)  # <method-wrapper '__str__' of Robot object at 0x10678c890>
print(droid1.__str__())  # <__main__.Robot object at 0x10698c790>

droid1()
