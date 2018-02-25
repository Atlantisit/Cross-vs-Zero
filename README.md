Tic Tac Toe game.

__Function list:__

_`instruct()`_ - instruction for the game;\n

_`ask_yes_no(question)`_ - accepts text, returns 'y' or 'n';

_`ask\_number(question, low, higt())`_ - accepts text, returns an integer in the range low-hight;

_`chip()`_ - Choose who plays first. Returns types of chips (X or 0);

_`new_board()`_ - creates a new game board, return the board;

_`available_moves()`_ -  creates a list of available moves. Accepts the board, returns a list of available moves;

_`winner(board)`_ - print the winner of the game. Accepts the board, returns type of the winner chips (X or O), or a draw;

_`human_move(board, human)`_ - human player's move. Accepts the board, type of player's chips, returns the human player's move;

_`computer_move(board, computer, human)`_ - Accepts the board, type of chips player's, return computer's move;

_`next_turn(turn)`_ - Accepts the types of chips, return types of chips;

_`congrat_winner(the_winner, computer, human)`_ - Declare the winner, or ascertains a draw. Accepts the types of chips.