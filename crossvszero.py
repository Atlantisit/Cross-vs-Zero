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
def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "-------------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "-------------")
    print("\t", board[6], "|", board[7], "|", board[8], "/n")
def available_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                    (3, 4, 5),
                    (6, 7, 8),
                    (0, 3, 6),
                    (1, 4, 7),
                    (2, 5, 8),
                    (0, 4, 8),
                    (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None 
def human_move(board, human):
    legal = display_board(board)
    move = None
    while move not in legal:
        move = ask_number("Your move. Choose one of the field 1-8: ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThis field is busy. Choose other field.")
        print ("Ok")
        return move
