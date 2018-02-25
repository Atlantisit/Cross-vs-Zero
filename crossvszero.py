# Function list:
# instruct() - instruction for game;
# ask_yes_no(question) - accept text, return 'y' or 'n';
# ask_number(question, low, higt()) - accept text, return an integer in the range low-hight;
# chip() - Choose who play first. Return tipes of chips (X or 0);
# new_board() - create new game board, return the board;
# available_moves() -  create list legal moves. Accepts the board, return list of available moves;
# winner(board) - print winner in the game. Accepts the board, return type of winner chips (X or O), or a draw.
# human_move(board, human) - human player's move. Accepts the board, type of chips player's, return human player's move;
# computer_move(board, computer, human) - Accepts the board, type of chips player's, return computer's move;
# next_turn(turn) - Accepts tupes of chips, return tupes of chips;
# congrat_winner(the_winner, computer, human) - Congrat the winner, or ascertains a draw. Accepts tupes of chips.