Tic Tac Toe game.

__Function list:__

_instruct()_ - instruction for the game;\n

_ask_yes_no(question)_ - accepts text, returns 'y' or 'n';

_ask\_number(question, low, higt())_ - accepts text, returns an integer in the range low-hight;

_chip()_ - Choose who plays first. Returns types of chips (X or 0);

_`new_board()`_ - creates a new game board, return the board;

available_moves() -  creates a list of available moves. Accepts the board, returns a list of available moves;

winner(board) - print the winner of the game. Accepts the board, returns type of the winner chips (X or O), or a draw;

human_move(board, human) - human player's move. Accepts the board, type of player's chips, returns the human player's move;

computer_move(board, computer, human) - Accepts the board, type of chips player's, return computer's move;

next_turn(turn) - Accepts the types of chips, return types of chips;

congrat_winner(the_winner, computer, human) - Declare the winner, or ascertains a draw. Accepts the types of chips.