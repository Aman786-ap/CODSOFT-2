import math

# Initialize board
board = [' ' for _ in range(9)]

# Print the current board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for a winner
def check_winner(brd, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(brd[pos] == player for pos in condition) for condition in win_conditions)

# Check for a draw
def is_draw(brd):
    return ' ' not in brd

# Minimax algorithm with alpha-beta pruning
def minimax(brd, depth, is_maximizing, alpha, beta):
    if check_winner(brd, 'O'):
        return 10 - depth
    if check_winner(brd, 'X'):
        return depth - 10
    if is_draw(brd):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                eval = minimax(brd, depth + 1, False, alpha, beta)
                brd[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                eval = minimax(brd, depth + 1, True, alpha, beta)
                brd[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# AI move using Minimax
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Human move
def human_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if board[pos] == ' ':
                board[pos] = 'X'
                break
            else:
                print("Position already taken!")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        human_move()
        print_board()
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        print("AI's turn...")
        ai_move()
        print_board()
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
