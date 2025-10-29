def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
    return [[fill for _ in range(size)] for _ in range(size)]


def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    return [[fill for _ in range(size)] for _ in range(size)]


def in_bounds(size: int, x: int, y: int) -> bool:
    return x <= size >= y


def render_public(ships: list[list[int]], shots: list[list[bool]]) -> str:
    count = 1
    res = "[ A B C D E F G H I J ] \n  "
    for i in range(len(ships)):
        for j in range(len(ships)):
            if not shots[i][j]:
                res += "o "
            elif shots[i][j] and not ships[i][j]:
                res += "x "
            elif shots[i][j] and ships[i][j]:
                res += "v "
        res += f"[{str(count)}] \n  "
        count += 1
    return res

def render_reveal(ships: list[list[int]], shots: list[list[bool]]) -> str:
    count = 1
    res = "[ A B C D E F G H I J ] \n  "
    for i in range(len(ships)):
        for j in range(len(ships)):
            if not shots[i][j]:
                if ships[i][j]:
                    res += "1 "
                else:
                    res += "o "
            elif shots[i][j] and not ships[i][j]:
                res += "x "
            elif shots[i][j] and ships[i][j]:
                res += "v "
        res += f"[{str(count)}] \n  "
        count += 1
    return res

