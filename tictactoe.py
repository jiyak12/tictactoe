import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O

def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    if action not in actions(board):
        raise ValueError("Invalid action")
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

def terminal(board):
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)

def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0

def minimax(board):
    if terminal(board):
        return None
    
    def max_value(board, alpha, beta):
        if terminal(board):
            return utility(board), None
        v = -math.inf
        best_action = None
        for action in actions(board):
            min_result, _ = min_value(result(board, action), alpha, beta)
            if min_result > v:
                v, best_action = min_result, action
            alpha = max(alpha, v)
            if alpha >= beta:
                break  
        return v, best_action
    
    def min_value(board, alpha, beta):
        if terminal(board):
            return utility(board), None
        v = math.inf
        best_action = None
        for action in actions(board):
            max_result, _ = max_value(result(board, action), alpha, beta)
            if max_result < v:
                v, best_action = max_result, action
            beta = min(beta, v)
            if beta <= alpha:
                break  
        return v, best_action
    
    current_player = player(board)
    return max_value(board, -math.inf, math.inf)[1] if current_player == X else min_value(board, -math.inf, math.inf)[1]
