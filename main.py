from submarines.game import init_game,shoot,is_won,is_lost
from submarines.io import print_end,print_status,parse_coords
from submarines.placement import place_random_ships

def play(size: int = 10, n_ships: int = 17, max_shots: int = 50) -> None:
    mange_game = init_game(size,n_ships,max_shots)
    place_random_ships(mange_game["ships"])
    while True:
        print_status(mange_game)
        column_input = input("please enter a column coordination: ")
        row_input = input("please enter a row coordination: ")
        check_coordination = parse_coords(row_input,column_input)

        if check_coordination:
            shoot(mange_game,check_coordination[0],check_coordination[1])
            print_end(mange_game,is_won(mange_game),is_lost(mange_game))
            if is_won(mange_game) or is_lost(mange_game):
                break



if __name__ == "__main__":
    play()