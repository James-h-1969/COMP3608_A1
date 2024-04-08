from part2 import connect_four_ab, game_over
from part3 import connect_four_final
from part1 import connect_four_mm
from part3b import connect_four_final_2

def make_move(state, column, colour):
    i = 1
    collision = False
    while i  < 6 and not collision:
        collision = state[i][column] != "."
        i += 1
    i -= 2 if collision else 1
    state[i] = state[i][:column] + colour + state[i][column+1:]
    return state

start_state = ".......,.......,.......,.......,.......,......."
start_state = start_state.split(",")
start_state.reverse()
play_1 = True
p = "r"

while(not game_over(start_state, p)):
    start_state.reverse()
    other_start = ",".join(start_state)
    start_state.reverse()
    for row in start_state:
        for char in row:
            print("\U0001F534" if char == 'r' else "\U0001F7E1" if char == 'y' else "\U0001F518", end="")
        print()
    print()
    if play_1:
        # move = input("MOVE: ")
        # move += "\nhi"
        move = connect_four_final(other_start, "red", 6)
        if "." not in other_start:
            print("TIE OCCURED")
            exit()
        start_state = make_move(start_state, int(move.split("\n")[0]), "r")
    else:
        move = connect_four_final_2(other_start, "yellow", 6)
        if "." not in other_start:
            print("TIE OCCURED")
            exit()
        start_state = make_move(start_state, int(move.split("\n")[0]), "y")
    play_1 = not play_1
    p =  "r" if p == "y" else "y"



if play_1:
    print("DUMB BOT WINS!")
else:
    print("SMART BOT WINS!")


    
    