from typing import List, Tuple, Dict

# 타입 힌트: 타입 힌트이기 때문에 따로 타입을 검사하지는 않는다.
int_var: int = 88
str_var: str = "hello world"
float_var: float = 88.9
bool_var: bool = True

list_var: List[int] = [1, 2, 3]
list_var: List[str] = ["1", "2", "3"]

tuple_var: Tuple[int, ...] = (1, 2, 3)
dic_var: Dict[str, int] = {"hello": 47}


# isinstance(obj, class): 해당 obj가 class의 인스턴스인지 아닌지 checking
# print(isinstance(88, int))  # True
# print(isinstance(88, float))  # True
# print(isinstance(False, bool))  # True


def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error: {typer}")


def cal_add(x: int, y: int) -> int:
    type_check(x, int)
    type_check(y, int)
    return x + y


print(cal_add(1, 3))  # 4
# print(cal_add("1", "3"))  # Error
# print(cal_add([1, 3], [4, 5])) # Error
