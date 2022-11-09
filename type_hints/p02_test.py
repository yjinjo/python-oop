# 명령어: pyright p02_test.py && python3 p02_test.py
# 타입 체킹과 출력결과를 따로 테스트한다.


def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error: {typer}")


def cal_add(x: int, y: int) -> int:
    type_check(x, int)
    type_check(y, int)
    return x + y


cal_add(1, 3)  # 4
