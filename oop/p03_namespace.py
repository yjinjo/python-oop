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


siri = Robot("siri")
jarvis = Robot("jarvis")
bixby = Robot("bixby")

print(Robot.__dict__)

print(siri.__dict__)  # {'name': 'siri'}

print(jarvis.__dict__)  # {'name': 'jarvis'}

print(siri.name)  # siri
print(bixby.name)  # bixby
print(siri.cal_add(2, 3))  # 5

print(siri.population)  # 3
siri.how_many()  # We have 3 robots.

Robot.say_hi(siri)  # Greetings, my masters call me siri.
siri.say_hi()  # Greetings, my masters call me siri.

print(dir(siri))
print(dir(Robot))

print(Robot.__doc__)

print(siri.__class__)  # <class '__main__.Robot'>
