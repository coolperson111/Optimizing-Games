import random
import os


def initialize(board):
    print("CONNECT 4!!\n You : 'X'\n CPU : 'O'\n")
    for i in range(6):
        for j in range(7):
            board[i][j] = ' '
        os.system("clear")
    print_board(board)


def print_board(board):
    os.system("clear")
    print("\n   1   2   3   4   5   6   7\n   |   |   |   |   |   |   |\n   V   V   V   V   V   V   V\n")
    for i in range(6):
        for j in range(7):
            print(f" | {board[i][j]}", end='')
        print(" |")
    print(" -----------------------------")


def player_input(board):
    while True:
        column = int(input("Enter your slot (1-7): ")) - 1
        if 0 <= column < 7 and board[0][column] == ' ':
            for i in range(5, -1, -1):
                if board[i][column] == ' ':
                    board[i][column] = 'X'
                    break
            break
        else:
            print("Invalid input. Try again.")
    print_board(board)


def cpu_input(board):
    while True:
        is_full = False
        column = random.randint(0, 6)
        if board[0][column] != ' ':
            is_full = True
        if not is_full:
            for i in range(5, -1, -1):
                if board[i][column] == ' ':
                    board[i][column] = 'O'
                    break
            break
    print_board(board)


def check_winner(board):
    winner = ' '
    # Vertical check
    for i in range(3):
        for j in range(7):
            if board[i][j] != ' ' and board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j]:
                winner = board[i][j]
    # Horizontal check
    for i in range(6):
        for j in range(4):
            if board[i][j] != ' ' and board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3]:
                winner = board[i][j]
    # Diagonal right->left
    for i in range(3):
        for j in range(4):
            if board[i][j] != ' ' and board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3]:
                winner = board[i][j]
    # Diagonal left->right
    for i in range(3):
        for j in range(3, 7):
            if board[i][j] != ' ' and board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] == board[i + 3][j - 3]:
                winner = board[i][j]
    return winner


def main():
    board = [[' ' for _ in range(7)] for _ in range(6)]
    winner = ' '
    initialize(board)

    for i in range(42):
        if i % 2 == 1:
            cpu_input(board)
        else:
            player_input(board)
        winner = check_winner(board)

        if winner == 'X':
            print("\n************\n|You win!!!|\n************")
            break
        elif winner == 'O':
            print("\n*************\n|CPU wins!!!|\n*************")
            break

    if winner == ' ':
        print("\n**********\n|DRAW!!!|\n**********")


if __name__ == "__main__":
    main()

