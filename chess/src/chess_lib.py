import chess
from stockfish import Stockfish


fish = Stockfish(
        path="/home/malhar/.local/Programs/stockfish/src/stockfish",
        depth=1,
        parameters={"Threads": 1,
                    "Ponder": "false",
                    "Contempt": 0,
                    "Skill Level": 0,
                    }
        )

piece_symbols = {
    chess.Piece(chess.KING, chess.BLACK): '♔',
    chess.Piece(chess.QUEEN, chess.BLACK): '♕',
    chess.Piece(chess.ROOK, chess.BLACK): '♖',
    chess.Piece(chess.BISHOP, chess.BLACK): '♗',
    chess.Piece(chess.KNIGHT, chess.BLACK): '♘',
    chess.Piece(chess.PAWN, chess.BLACK): '♙',
    chess.Piece(chess.KING, chess.WHITE): '♚',
    chess.Piece(chess.QUEEN, chess.WHITE): '♛',
    chess.Piece(chess.ROOK, chess.WHITE): '♜',
    chess.Piece(chess.BISHOP, chess.WHITE): '♝',
    chess.Piece(chess.KNIGHT, chess.WHITE): '♞',
    chess.Piece(chess.PAWN, chess.WHITE): '♟',
    None: '  '
}


def print_board(board, move):
    print('\033[H\033[J', end="")
    print("      A   B   C   D   E   F   G   H")
    print("   +--------------------------------+")
    for i in range(8, 0, -1):
        print(f" {i} |", end=" ")
        for j in range(1, 9):
            square = chess.square(j - 1, i - 1)
            piece = board.piece_at(square)
            if piece is not None:
                print(f" {piece_symbols.get(piece)} ", end="")
            else:
                print("   ", end="")
            print("|", end="")
        print()
        print("   +--------------------------------+")
    print("      A   B   C   D   E   F   G   H")
    print("Previous move:", move)


def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    legal_moves = list(board.legal_moves)

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None

        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)[0]
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move

    else:
        min_eval = float('inf')
        best_move = None

        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)[0]
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move


def evaluate_board(board):
    piece_values = {
        chess.PAWN: 100,
        chess.KNIGHT: 320,
        chess.BISHOP: 330,
        chess.ROOK: 500,
        chess.QUEEN: 900,
        chess.KING: 20000
    }

    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            score += (piece_values[piece.piece_type] *
                      (1 if piece.color == chess.WHITE else -1))

    return score


def bot_move(board):
    opening_moves = ["e2e4", "g1f3", "d2d4"]
    depth = 3
    if board.fullmove_number < 4:
        return chess.Move.from_uci(opening_moves[board.fullmove_number-1])
    else:
        _, best_move = minimax(board, depth, float('-inf'), float('inf'), True)
        return best_move


def stockfish_move(board, depth=20):
    max_time = 500
    fish.set_fen_position(board.fen())

    best_move = fish.get_best_move_time(time=max_time)
    print(best_move)

    return best_move


def main():
    board = chess.Board()
    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move = bot_move(board)
            board.push(move)
            print_board(board, move)
        else:
            # user_move = input("Enter your move in UCI notation: ")
            user_move = stockfish_move(board)
            try:
                board.push_uci(user_move)
                print_board(board, move)
            except ValueError:
                print("Invalid move, try again.")

    print("Game over. Result:", board.result())
    print(board.fullmove_number)


if __name__ == "__main__":
    main()
