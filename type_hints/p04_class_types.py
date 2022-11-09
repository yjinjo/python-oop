class Hello:
    def world(self) -> int:
        return 7


class World:
    pass


# 클래스에 대한 인스턴스를 typing 해줄 때 클래스명을 적으면 된다.
hello: Hello = Hello()
world: World = World()


def foo(ins: Hello) -> int:
    return ins.world()


print(foo(hello))
# print(foo(world))  # error
