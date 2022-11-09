from typing import Union, List, Tuple, Dict, Optional
from typing_extensions import TypedDict

# Value = Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]]

# value: Value = 17


# def cal(v: Value) -> Value:
#     # 연산을 거친 뒤
#     return v


# Dictionary alias
ddd: Dict[str, Union[str, int]] = {"hell": "world", "world": "wow!!", "hee": 17}


class Point(TypedDict):
    x: int
    y: float
    z: str
    hello: int


point: Point = {"x": 8, "y": 8.4, "z": "hello", "hello": 12}
