tic_tac_toe_board = [[" "," "," "],
                     [" "," "," "],
                     [" "," "," "]]


def print_board():
    print("\n---------")
    for x in tic_tac_toe_board:
        for y in x:
            print(f"|{y}|",end="")
        print("\n---------")

# Check the board to see if there is a winner
# returns True if a winner is found and False if no winner yet
def check_board(cur_player):
    # check diagonals (2)
    if check_location(1,1,cur_player): #center
        if check_location(0,0,cur_player): #top left
            if check_location(2,2,cur_player): #bottom right
                print("Win Diagonal: top left")
                return True
        if check_location(0,2,cur_player): #bottom left
            if check_location(2,0,cur_player): #top right
                print("Win Diagonal bottom left")
                return True
            else:
                return False

    # check horizonals (3)
    for x in range(0,3):
        if check_location(x,0,cur_player):
            if check_location(x,1,cur_player):
                if check_location(x,2,cur_player):
                    # print(f"Win Horizontal {x}")
                    return True
                else:
                    return False
            else:
                return False

    # check verticals (3)
    for y in range(0,3):
        if check_location(0,y,cur_player):
            if check_location(1,y,cur_player):
                if check_location(2,y,cur_player):
                    # print(f"Win Vertical: {y}")
                    return True
                else:
                    return False
            else:
                return False
    return False

# Checks a specific location on the board
# returns true if that location has that player's mark
# used for checking the winning condition
def check_location(x,y,player):
    if tic_tac_toe_board[x][y] == player:
        # print(f"Loc: {tic_tac_toe_board[x][y]}")
        return True
    else:
        return False

# Recursive function that has the player select a location on the board to play
# returns the player's mark if the spot is empty
# recursively calls the function if the spot is already taken
def player_choose(player,loc,value,dif):
    if tic_tac_toe_board[loc][value-dif] == " ":
        return player
    else:
        x_place = int(input("Location already chosen, please choose again> "))
        return player_choose(player,loc,x_place,dif)

game = True
winner = ""
spots_left = 9
while game:
    print_board()
    # Player 1's turn to select a location
    x_place = int(input("Player 1: Please select a square by number> "))
    if x_place <=3:
        tic_tac_toe_board[0][x_place-1] = player_choose("X",0,x_place,1)
        spots_left -= 1
    elif x_place <= 6:
        tic_tac_toe_board[1][x_place-4] = player_choose("X",1,x_place,4)
        spots_left -= 1
    else:
        tic_tac_toe_board[2][x_place-7] = player_choose("X",2,x_place,7)
        spots_left -= 1
    print_board()
    if check_board("X"):
        game = False
        winner = "X"
    # if Player 1 did not already win, Player 2 gets a turn
    if game:
        o_place = int(input("Player 2: Please select a square by number> "))
        if o_place <= 3:
            tic_tac_toe_board[0][o_place-1] = player_choose("O", 0, o_place, 1)
            spots_left -= 1
        elif o_place <= 6:
            tic_tac_toe_board[1][o_place - 4] = player_choose("O", 1, o_place, 4)
            spots_left -= 1
        else:
            tic_tac_toe_board[2][o_place-7] = player_choose("O", 2, o_place, 7)
            spots_left -= 1
        if check_board("O"):
            game = False
            winner = "O"
        if spots_left == 0:
            game = False

if not winner == "":
    print(f"The winner is {winner}!")
else:
    print("There is no winner. Cats Game.")
print_board()