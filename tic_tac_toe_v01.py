import random

# DISPLAY THE TIC TAC TOE BOARD
def display_board(SPOTS):

    print(SPOTS[7] + "|" + SPOTS[8] + "|" + SPOTS[9])
    print(SPOTS[4] + "|" + SPOTS[5] + "|" + SPOTS[6])
    print(SPOTS[1] + "|" + SPOTS[2] + "|" + SPOTS[3])

# ALLOW THE USER TO PICK EITHER "X" OR "O"
def get_user_symbol():

    symbol = ''

    while symbol != "X" and symbol != "O":
        symbol = input("Please choose 'X' or 'O': ").upper()

    if symbol == "X":
        return ("X", "O")
    else:
        return ("O", "X")


# CHECK IF THE DESIRED SPOT IS OPEN
def check_spot_open(BOARD, POSITION):

    return BOARD[POSITION] == "_" 

# PLACE THE SYMBOL AT CHOSEN POSITION
def place_symbol(BOARD, SYMBOL, POSITION):

    BOARD[POSITION] = SYMBOL

# GET THE PLAYERS POSITION
def get_user_position(BOARD):

    pos = ''
    possible_pos = list(range(1,10))

    while pos not in possible_pos or not check_spot_open(BOARD, pos):
        pos = int(input("Please choose a position 1-9: "))

    return pos

# CHECK TO SEE IF ANYONE HAS WON
def check_won(BOARD, SYMBOL):
    return ((board[7] == board[8]== board[9] == SYMBOL or
    board[4] == board[5] == board[6] == SYMBOL or
    board[1] == board[2] == board[3] == SYMBOL or
    board[7] == board[4] == board[1] == SYMBOL or
    board[8] == board[5] == board[2] == SYMBOL or
    board[9] == board[6] == board[3] == SYMBOL or
    board[7] == board[5] == board[3] == SYMBOL or
    board[9] == board[5] == board[1] == SYMBOL))

# CHECK TO SEE IF THE BOARD IS FULL
def check_board_full(BOARD):

    for num in range(1,10):
        if BOARD[num] == "_":
            return False
    return True

# CHECK TO SEE IF THE PLAYER WANTS TO PLAY AGAIN
def replay():
    replay = input("Would you like to play again[Y/n?]").upper()

    if replay == "Y":
        return True
    else:
        return False

#### FINALLY RUN THE GAME

print("Welcome to Tic Tac Toe!")

game_on = True

while game_on:

    board1 = ['#', "1","2","3","4","5","6","7","8","9"]
    board = ['#', "_","_","_","_","_","_","_","_","_"]

    display_board(board1)

    player1, player2 = get_user_symbol()

    first = random.randint(0,1)
    if first == 0:
        turn = player1
    else:
        turn = player2
    print(turn + " will go first!")

    play = True

    while play:
        if turn == player1:
            pos = get_user_position(board)
            place_symbol(board,player1,pos)
            display_board(board)
            if check_won(board, player1):
                print("Player1 has won!")
                play = False
            if check_board_full(board):
                print("Tie game!")
                play = False
            turn = player2
        else:
            pos = get_user_position(board)
            place_symbol(board,player2,pos)
            display_board(board)
            if check_won(board, player2):
                print("Player2 has won!")
                play = False
            if check_board_full(board):
                print("Tie game!")
                play = False
            turn = player1

    if replay():
        pass
    else:
        game_on = False

            
