from submarines.board import render_public ,render_reveal
from submarines.game import remaining_ships ,shots_left

def parse_coords(row:str, column:str) -> tuple[int,int] | None:
    alpha = ["a","b","c","d","e","f","g","h","i","j"]
    column = column.lower()

    if column.isalpha() and column in alpha:
        column = (alpha.index(column))
    else:
        return None

    if row.isdigit():
        row = int(row)-1
    else:
        return None

    return row,column



def print_status(state: dict) -> None:
    print(f"you have mor {shots_left(state)} shots")
    print(f"There are {remaining_ships(state)} more ship compartments left.")
    print()
    print(render_public(state["ships"],state["shots"]))
    return


def print_end(state: dict,won :bool,lost:bool) -> None:
    if won:
        print("you won :)")
        print(render_reveal(state["ships"], state["shots"]))
    if lost:
        print("you lose :(")
        print(render_reveal(state["ships"], state["shots"]))
    return

