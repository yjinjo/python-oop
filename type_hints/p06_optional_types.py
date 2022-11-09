from typing import Union, Optional


def foo(name: str) -> Optional[str]:
    if name == "amamov":
        return None
    else:
        return name


# xxx: Union[str, None] = "amamov"
xxx: Optional[str] = foo("amamov")
