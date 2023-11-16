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
        print()
        print("   +--------------------------------+")
    print("      A   B   C   D   E   F   G   H")


chess_board = {}

chess_board[(1, 5)] = K
chess_board[(8, 2)] = k
chess_board[(7, 4)] = Q
chess_board[(2, 7)] = q
chess_board[(4, 4)] = P
chess_board[(5, 3)] = p

print_board(chess_board)
