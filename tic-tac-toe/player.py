from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def get_move(self):
        pass

    @abstractmethod
    def get_piece(self):
        pass

class HumanPlayer(Player):
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece

    def get_move(self):
        while True:
            try:
                move = input(f"{self.name} ({self.piece}), enter your move (row, col): ")
                row, col = map(int, move.split(","))
                return row, col
            except ValueError:
                print("Invalid input! Please enter row and column separated by a comma (e.g., 0,1).")

    def get_piece(self):
        return self.piece
