def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def show_positions():
    print("Positions are numbered 1 to 9 as below:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")
    print()

def is_valid_move(board, move):
    return move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == ' '

def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for i, j, k in win_conditions:
        if board[i] == board[j] == board[k] == player:
            return True
    return False

def is_draw(board):
    return ' ' not in board

def minimax(board, depth, is_ai):
    if check_winner(board, 'O'):
        return 10 - depth
    if check_winner(board, 'X'):
        return depth - 10
    if is_draw(board):
        return 0

    if is_ai:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def make_ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'
    return best_move + 1

def main():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")
    show_positions()
    print_board(board)

    while True:
        move = input("Enter your move (1-9): ")
        if not is_valid_move(board, move):
            print("Please enter a valid number.")
            print_board(board)
            continue

        move = int(move) - 1
        board[move] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        ai_pos = make_ai_move(board)
        print(f"AI placed O at position {ai_pos}")
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
