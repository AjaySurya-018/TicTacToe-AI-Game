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
    # Count the number of X and number of O in the board.
    num_X = sum(row.count("X") for row in board)
    num_O = sum(row.count("O") for row in board)

    # Check if the game is over
    if terminal(board):
        return None
    
    # Determining the current player based on number of X and O 
    if num_X == num_O:
        return 'X'
    else:
        return 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Initialize an empty set to store valid actions
    valid_actions = set()

    # Iterate through the board to find empty cells
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                valid_actions.add((i, j))

    return valid_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Make a shallow copy of the original board
    new_board = [row[:] for row in board]

    # Get the current player (X or O)
    current_player = player(board)

    # Check if the action is valid
    if action not in actions(board):
        raise Exception("Invalid action!")

    # Apply the action to the new board
    i, j = action
    new_board[i][j] = current_player

    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows for a win
    for row in board:
        if row.count('X') == 3:
            return 'X'
        elif row.count('O') == 3:
            return 'O'

    # Check columns for a win
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == 'X':
            return 'X'
        elif board[0][j] == board[1][j] == board[2][j] == 'O':
            return 'O'

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
        return 'X'
    elif board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        return 'O'

    # No winner found, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there is a winner
    if winner(board) is not None:
        return True

    # Check if all cells are filled
    for row in board:
        if EMPTY in row:
            return False

    # If no winner and all cells are filled, the game is over
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Get the winner of the game
    winner_player = winner(board)

    # Determine the utility based on the winner
    if winner_player == 'X':
        return 1
    elif winner_player == 'O':
        return -1
    else:
        return 0
    
def minimax(board):
    # If the game is over, return None (terminal board)
    if terminal(board):
        return None

    # Get the current player (X or O)
    current_player = player(board)

    # Initialize variables to keep track of best move and best utility value
    best_move = None
    best_utility = float('-inf') if current_player == 'X' else float('inf')

    # Iterate over all possible actions
    for action in actions(board):
        # Calculate the utility value for the current action
        utility_value = min_value(result(board, action), float('-inf'), float('inf'))

        # Update the best move and best utility value
        if current_player == 'X':
            if utility_value > best_utility:
                best_utility = utility_value
                best_move = action
        else:
            if utility_value < best_utility:
                best_utility = utility_value
                best_move = action

    return best_move


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return v


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v







