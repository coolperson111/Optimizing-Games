chess_board = {}

K = '♚'
Q = '♛'
R = '♜'
B = '♝'
N = '♞'
P = '♟'

k = '♔'
q = '♕'
r = '♖'
b = '♗'
n = '♘'
p = '♙'


def print_board(board):
    print('\033c')
    print("      A   B   C   D   E   F   G   H")
    print("   +--------------------------------+")
    for i in range(8, 0, -1):
        print(f" {i} |", end=" ")
        for j in range(1, 9):
            piece = board.get((i, j), " ")
            print(f" {piece} ", end="")
            print("|", end="")
        print(f" {i}")
        print("   +--------------------------------+")
    print("      A   B   C   D   E   F   G   H")


K = '♚'
Q = '♛'
R = '♜'
B = '♝'
N = '♞'
P = '♟'

k = '♔'
q = '♕'
r = '♖'
b = '♗'
n = '♘'
p = '♙'

chess_board = {}

def print_board():
    print('\033c')
    print("      A   B   C   D   E   F   G   H")
    print("   +--------------------------------+")
    for i in range(8, 0, -1):
        print(f" {i} |", end=" ")
        for j in range(1, 9):
            piece = chess_board.get((i, j), " ")
            print(f" {piece} ", end="")
            print("|", end="")
        print()
        print("   +--------------------------------+")
    print("      A   B   C   D   E   F   G   H")


def make_move(move, player):
    from_square = (int(move[1]), ord(move[0])-96)
    to_square = (int(move[3]), ord(move[2])-96)

    '''
    if chess_board.get(from_square) is None or (player == 1 and chess_board[from_square].isupper()) or (player == 2 and chess_board[from_square].islower()):
        print("Invalid move. Try again.")
        return
    '''

    chess_board[to_square] = chess_board[from_square]
    del chess_board[from_square]

def play_chess():

    player_turn = 1

    while True:
        print_board()
        player = f"Player {player_turn}"

        move = input(f"{player}, enter your move (type 'q' to quit): ").lower()

        if move == 'q':
            print("Game over. Thanks for playing!")
            break

        if len(move) == 4:
            make_move(move, player_turn)
            player_turn = 3 - player_turn  # Switch between 1 and 2
        else:
            print("Invalid input. Please enter a valid move.")


def main():
    chess_board[(1, 5)] = K
    chess_board[(8, 2)] = k
    chess_board[(7, 4)] = Q
    chess_board[(2, 7)] = q
    chess_board[(4, 4)] = P
    chess_board[(5, 3)] = p

    print_board()
    play_chess()


if __name__ == "__main__":
    main()

