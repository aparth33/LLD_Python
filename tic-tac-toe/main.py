from player import HumanPlayer
from board import Board
from game import Game

def main():
    # Get number of players and board size from the user
    try:
        num_players = int(input("Enter the number of players: "))
        board_size = int(input("Enter the size of the board (e.g., 3 for 3x3): "))
    except ValueError:
        print("Invalid input, using default values (2 players, 3x3 board).")
        num_players = 2
        board_size = 3

    # Initialize the board
    game_board = Board(board_size)

    # Create players dynamically based on input
    players = []
    used_symbols = set()

    for i in range(num_players):
        while True:
            piece = input(f"Enter symbol for Player {i+1}: ").strip()
            if piece and piece not in used_symbols:
                used_symbols.add(piece)
                break
            else:
                print("Symbol already taken or invalid, please choose another symbol.")

        name = input(f"Enter name for Player {i+1}: ")
        players.append(HumanPlayer(name, piece))

    # Initialize the game
    game = Game(players, game_board)

    # Start the game
    game.play()

if __name__ == "__main__":
    main()