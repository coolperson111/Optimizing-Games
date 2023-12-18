import chess
import chess.svg
from cairosvg import svg2png
from PIL import Image, ImageTk
import tkinter as tk
import io

# Initialize the board
board = chess.Board()
selected_square = None


def display_board(board):
    svg_text = chess.svg.board(board=board)
    png_output = svg2png(bytestring=svg_text)
    img_stream = io.BytesIO(png_output)
    img = Image.open(img_stream)
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo


def handle_click(event):
    global board, selected_square
    col_size = root.winfo_width() / 8
    row_size = root.winfo_height() / 8

    col = int(event.x // col_size)
    row = 7 - int(event.y // row_size)  # Invert the row to match chess coordinates

    square = chess.square(col, row)

    if selected_square is None:
        if board.piece_at(square) is None or board.piece_at(square).color != board.turn:
            return
        selected_square = square
    else:
        move = chess.Move(selected_square, square)
        if move in board.legal_moves:
            board.push(move)
        else:
            print("Invalid move. Please try again.")
        selected_square = None

    display_board(board)


# Create Tkinter window
root = tk.Tk()
root.title("Chess Game")

# Create Tkinter Label to display the chess board
label = tk.Label(root)
label.pack(expand=True, fill="both")

# Display initial board
display_board(board)

# Bind left mouse click to handle_click function
label.bind("<Button-1>", handle_click)

# Start the Tkinter main loop
root.mainloop()

