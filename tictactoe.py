"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count <= o_count:
        return X
    else:
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.

    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
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

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if all(cell is not EMPTY for row in board for cell in row):
        return True
    return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    current = player(board)
    if current == X:
        best_val = -math.inf
        best_move = None
        for action in actions(board):
            val = min_value(result(board, action))
            if val > best_val:
                best_val = val
                best_move = action
        return best_move
    else:
        best_val = math.inf
        best_move = None
        for action in actions(board):
            val = max_value(result(board, action))
            if val < best_val:
                best_val = val
                best_move = action
        return best_move
    raise NotImplementedError
