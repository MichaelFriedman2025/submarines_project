import random

def place_ship_if_valid(board: list[list[int]], start_row: int, start_col: int, ship_length: int, direction: int) -> bool:
    board_size = len(board)

    for i in range(ship_length):
        current_row = ''
        current_col = ''

        if direction == 1:
            current_row = start_row + i
            current_col = start_col
        elif direction == 2:
            current_row = start_row
            current_col = start_col + i

        if current_row < 0 or current_row >= board_size or current_col < 0 or current_col >= board_size:
            return False

        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
                neighbor_row = current_row + row_offset
                neighbor_col = current_col + col_offset

                if 0 <= neighbor_row < board_size and 0 <= neighbor_col < board_size:
                    if board[neighbor_row][neighbor_col]:
                        return False

    for i in range(ship_length):
        if direction == 1:
            current_row = start_row + i
            current_col = start_col
        else:
            current_row = start_row
            current_col = start_col + i

        board[current_row][current_col] = 1

    return True

def place_random_ships(ships: list[list[int]]) -> None:
    all_ships = [2,3,3,4,5]
    while all_ships:
        row_index = random.randint(0,9)
        column_index = random.randint(0,9)
        direction = random.randint(1,2)

        all_ships_pop = place_ship_if_valid(ships,row_index,column_index,all_ships[-1],direction)
        if all_ships_pop:
            all_ships.pop()
    return

