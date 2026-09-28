import math

board = [" "] * 9


def print_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def is_draw():
    return " " not in board


def minimax(is_maximizing):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = ""
                best_score = min(best_score, score)

        return best_score


def best_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


print("===== TIC-TAC-TOE AI =====")
print("You = X")
print("AI  = O")

while True:
    print_board()

    try:
        position = int(input("Enter position (1-9): ")) - 1

        if position < 0 or position > 8:
            print("Please enter a number between 1 and 9.")
            continue

        if board[position] != " ":
            print("Position already occupied!")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    board[position] = "X"

    if check_winner("X"):
        print_board()
        print("You win!")
        break

    if is_draw():
        print_board()
        print("Game Draw!")
        break

    ai_position = best_move()
    board[ai_position] = "O"

    print("AI selected position:", ai_position + 1)

    if check_winner("O"):
        print_board()
        print("AI wins!")
        break

    if is_draw():
        print_board()
        print("Game Draw!")
        break