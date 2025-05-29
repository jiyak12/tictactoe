# Tic-Tac-Toe Game using Minimax 
In this repository, we will implement an AI to play Tic-Tac-Toe optimally using Minimax algorithm.
## Understanding
- There are two main files in this project: `runner.py` and `tictactoe.py`.
- `tictactoe.py` contains all of the logic for playing the game, and for making optimal moves.
- `runner.py` contains all of the code to run the graphical interface for the game.
## Specification
- The `player` function takes a board state as input, and return which player’s turn it is (either X or O). In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
- The `actions` function returns a set of all of the possible actions that can be taken on a given board. Each action is represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
Possible moves are any cells on the board that do not already have an X or an O in them. Any return value is acceptable if a terminal board is provided as input.
- The `result` function takes a board and an action as input, and returns a new board state, without modifying the original board. If action is not a valid action for the board, your program raises an exception.
The returned board state is the board that results from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.
Importantly, the original board is left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell on board itself is not a correct implementation of the result function. So a deep copy of the board is made first before making any changes.
- The `winner` function accepts a board as input, and return the winner of the board if there is one. If X wins the game, function returns X and vice versa. One can win the game with three of their moves in a row horizontally, vertically, or diagonally. There is atmost one winner. In case of no winner, function returns None.
- The `terminal` function accepts a board as input, and return a boolean value indicating whether the game is over. If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function returns True. Otherwise, the function returns False if the game is still in progress.
- The `utility` function accepts. a terminal board as input and output the utility of the board. If X wins, the utility is 1. If O has wins, the utility is -1. If the game ends in a tie, the utility is 0.
Utility will only be called on a board if terminal(board) is True.
- The `minimax` function takes a board as input, and returns the optimal move for the player to move on that board.
The move returned is the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
If the board is a terminal board, the minimax function returns None.
## Prerequisites
- Install the required dependencies using: `pip3 install -r requirements.txt`
- Run the game using: `python runner.py`
## Game Representation
- The board is represented as a 3x3 grid where each cell is X, O, or EMPTY.
- The game starts with an empty board, and players alternate turns.
## Implementation of Minimax algorithm with alpha-beta pruning
- The AI evaluates all possible moves and chooses the one that maximizes its chances ofwinning or drawing.
- Alpha-Beta Pruning improves Minimax by eliminating branches that do not need to beexplored, significantly reducing computation time.
- The algorithm assigns values to terminal states:○ +1 for an X win○ -1 for an O win○ 0 for a tie
- The AI recursively simulates all possible moves and selects the optimal one whilepruning unnecessary branches.
## Images 
- Initial State:
- ![image](https://github.com/user-attachments/assets/fe7fc53e-937b-4e6d-8c4c-09209e24515e)
- The first move is made by X and then by O :
- ![image](https://github.com/user-attachments/assets/0b5a7118-60ba-4f2b-87ac-73f4e8fd6842)

- When it's a draw:
- ![image](https://github.com/user-attachments/assets/7d3f2902-7f83-4953-a8d2-0856b269131b)









 




