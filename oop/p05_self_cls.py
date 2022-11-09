class SelfTest:

    # 클래스 변수
    name = "amamov"

    def __init__(self, x):
        self.x = x

    # 클래스 메서드
    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print("func1")

    # 인스턴스 메서드
    def func2(self):
        print(f"self: {self}")
        print(f"class안의 self 주소: {id(self)}")
        print("func2")


test_obj = SelfTest(17)

SelfTest.func1()
test_obj.func2()  # class안의 self 주소: 4338532560

print(f"인스턴스의 주소: {id(test_obj)}")  # 인스턴스의 주소: 4338532560

test_obj.func1()

print(test_obj.name)  # amamov

# SelfTest.func2()  # 에러

# SelfTest.x  # 에러
