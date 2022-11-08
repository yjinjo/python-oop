class Robot:
    __population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Robot.__population += 1

    @property
    def get_name(self):
        return f"yoon {self.__name}"

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def set_age(self, new_age):
        if new_age < 0:
            raise TypeError("invalid range to age")
        self.__age = new_age

    def __say_hi(self):
        print(f"Greetings, my masters call me {self.__name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots.")


droid = Robot("R2-D2", 2)

print(droid.get_age)
droid.set_age = 7
print(droid.get_age)

print(droid.get_name)
