from player import Player
from board import Board
class Game:
    def __init__(self, players:list[Player], board:Board):
        self.players = players  # List of players, allowing for more than 2 players
        self.board = board
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play(self):
        while True:
            current_player = self.players[self.current_player_index]
            print("\nCurrent Board:")
            self.board.display()

            # Get the current player's move and place the piece
            row, col = current_player.get_move()
            if self.board.place_piece(row, col, current_player.get_piece()):
                if self.board.check_winner(current_player.get_piece()):
                    print(f"{current_player.name} wins!")
                    self.board.display()
                    break
                elif self.board.is_full():
                    print("It's a tie!")
                    self.board.display()
                    break
                else:
                    self.switch_player()
            else:
                print("Cell is already occupied, try again!")
