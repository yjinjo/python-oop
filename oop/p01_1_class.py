class Cal:

    # 클래스가 메모리에 올라왔을 때 := 클래스로 인스턴스를 하나 생성했을 때
    # 즉시 실행되는 함수이다.
    # (생성자: 메모리에 올라오는 순간 즉시 실행된다고 한다.)
    def __init__(self, a, b):
        # self: 클래스로 인스턴스를 만들었을 때 그 인스턴스를 지칭하는 것이다.
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


# 클래스로 인스턴스를 찍어내는 순간 메모리에 올라간다.
# 그럼, __init__ 메서드가 호출된다.
cal1 = Cal(1, 2)
# cal1이 곧 self가 되므로 self.a 를 가리키는 것이다.
print(cal1.a)  # 1
print(cal1.b)  # 2
print(cal1.add())  # 3
print(cal1.sub())  # -1
print(cal1.div())  # 0.5

print()

# namespace가 바뀌는 순간(self.a가 바뀌는 순간) 클래스 안에서의 모든 self.a가 바뀐다.
cal1.a = 7
# cal1이 곧 self가 되므로 self.a 를 가리키는 것이다.
print(cal1.a)  # 7
print(cal1.b)  # 2
print(cal1.add())  # 9
print(cal1.sub())  # 5
print(cal1.div())  # 3.5

print()

# 같은 쿠키틀(class)로 만들었다고 하더라도, 쿠키(인스턴스) cal1 과 cal2는 서로 독립적이다.
cal2 = Cal(3, 4)
print(cal2.a)  # 3
print(cal2.b)  # 4
print(cal2.add())  # 7
print(cal2.sub())  # -1
print(cal2.div())  # 0.75
