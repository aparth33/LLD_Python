class Board:
    def __init__(self, size=3):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * (self.size * 2 - 1))

    def is_full(self):
        return all(self.board[row][col] != " " for row in range(self.size) for col in range(self.size))

    def is_cell_empty(self, row, col):
        return self.board[row][col] == " "

    def place_piece(self, row, col, piece):
        if self.is_cell_empty(row, col):
            self.board[row][col] = piece
            return True
        return False

    def check_winner(self, piece):
        # Check rows
        for row in self.board:
            if all(cell == piece for cell in row):
                return True
        # Check columns
        for col in range(self.size):
            if all(self.board[row][col] == piece for row in range(self.size)):
                return True
        # Check diagonals
        if all(self.board[i][i] == piece for i in range(self.size)):
            return True
        if all(self.board[i][self.size - 1 - i] == piece for i in range(self.size)):
            return True
        return False
