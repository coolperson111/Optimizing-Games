import os

board = [" " for _ in range(9)]
player_token = "X"
bot_token = "O"


def print_board(board):
    os.system("clear")
    print(f'''
         |     |
      {board[0]}  |  {board[1]}  |  {board[2]}
    _____|_____|_____
         |     |
      {board[3]}  |  {board[4]}  |  {board[5]}
    _____|_____|_____
         |     |
      {board[6]}  |  {board[7]}  |  {board[8]}
         |     |
    ''')


def win(board, player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))


def fullboard(board):
    return " " not in board


def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == " ":
            return int(move) - 1
        else:
            print("Invalid move. Try again.")


def bot_move():
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = bot_token
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


def minimax(board, depth, maximising):
    if win(board, bot_token):
        return 1
    if win(board, player_token):
        return -1
    if fullboard(board):
        return 0

    if maximising:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = bot_token
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = player_token
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


def player_playgame():
    player_index = player_move()
    board[player_index] = player_token
    print_board(board)
    if win(board, player_token):
        print("You win!")
        return True
    if fullboard(board):
        print("It's a draw!")
        return True
    return False


def bot_playgame():
    bot_index = bot_move()
    board[bot_index] = bot_token
    print_board(board)
    if win(board, bot_token):
        print("Bot wins!")
        return True
    if fullboard(board):
        print("It's a draw!")
        return True
    return False


def main():
    print("Tic-Tac-Toe")
    print_board(board)
    while True:
        if player_playgame():
            break
        if bot_playgame():
            break


if __name__ == "__main__":
    main()
