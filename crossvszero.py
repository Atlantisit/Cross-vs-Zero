import random
#Global consts
X = 'X'
O = 'O'
EMPTY = " "
TIE = "A draw"
NUM_SQUARES = 9
#Part with functions
def instruct():
    print(
        """
        Wellcome to the game Tic-Tac-Toe!
        Look at this board:\n
        0 | 1 | 2
        3 | 4 | 5
        6 | 7 | 8
        \nEnter a number from 0 to 8 to make a move. Good luck!
        """
    )
def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question),lower()
    return response
def ask_number(question, low, high):
    response = None
    while respornse not in range (low, high):
        response = int(input(question))
        return response
def chip():
    number = random.choice((X,O))
    if number == X:
        print("Your move will be first!")
        human = X
    else:
        print("I will be first!")
        computer = X
def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
