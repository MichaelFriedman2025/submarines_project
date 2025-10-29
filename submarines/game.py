from submarines.board import create_matrix ,create_bool_matrix,in_bounds


def init_game(size: int, n_ships: int, max_shots: int) -> dict:
    return {
            "size":size,
            "ships":create_matrix(size),
            "shots":create_bool_matrix(size),
            "n_ships":n_ships,
            "max_shots":max_shots,
            "shots_used":0
            }


def shoot(state: dict, row: int, column: int) -> None:
    if in_bounds(state["size"],row,column):
        if state["shots"][row][column]:
            print("this place already shot :| try agen ")
        else:
            state["shots"][row][column] = True
            state["shots_used"] += 1
            if state["ships"][row][column]:
                state["n_ships"] -= 1
                print("good shot :)")
            else:
                print("you missed the ship :(")
    else:
        print("you shot out of bounds   :-[ ")
        return

def is_won(state: dict) -> bool:
    return not state["n_ships"] and shots_left(state)


def is_lost(state: dict) -> bool:
    return state["n_ships"] and not shots_left(state)

def shots_left(state: dict) -> int:
    return state["max_shots"] - state["shots_used"]


def remaining_ships(state: dict) -> int:
    return state["n_ships"]

