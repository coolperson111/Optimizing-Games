import chess
import chess.svg
from cairosvg import svg2png
import matplotlib.pyplot as plt
from PIL import Image
import io

# Initialize the board
board = chess.Board()
displayed_image = None  # Variable to hold the displayed image

def display_board(board, previous_image=None):
    # Generate SVG representation of the current board position
    svg_text = chess.svg.board(board=board)

    # Convert SVG to PNG in memory
    png_output = svg2png(bytestring=svg_text)

    # Convert PNG bytes to an in-memory binary stream
    img_stream = io.BytesIO(png_output)

    # Open the image using PIL
    img = Image.open(img_stream)

    # Display the image using matplotlib
    plt.figure()
    plt.imshow(img)
    plt.axis('off')  # Turn off axis labels
    plt.show(block=False)  # Show image and continue execution without blocking

    # Close the previous image if it exists
    if previous_image:
        plt.close(previous_image)

    return plt.gcf()  # Return the current figure

# Initial board display
displayed_image = display_board(board)

# Interactive gameplay loop
while not board.is_game_over():
    user_move = input("Enter your move in UCI format (e.g., 'e2e4'), 'exit' to quit: ")

    if user_move.lower() == 'exit':
        break

    try:
        move = chess.Move.from_uci(user_move)
        if move in board.legal_moves:
            board.push(move)
            displayed_image = display_board(board, displayed_image)
        else:
            print("Invalid move. This move is not allowed. Legal moves:", [str(move) for move in board.legal_moves])
    except ValueError:
        print("Invalid move format. Please provide moves in UCI format (e.g., 'e2e4').")

