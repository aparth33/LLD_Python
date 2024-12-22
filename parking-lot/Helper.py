class Helper:
    def get_spot_id(self, floor, row, col):
        """
        Generate a spot ID based on floor, row, and column.
        """
        return f"F{floor}R{row}C{col}"

    def get_spot_location(self, spot_id):
        """
        Parse the spot ID to extract the floor, row, and column.
        """
        try:
            floor = int(spot_id[1:spot_id.index("R")])
            row = int(spot_id[spot_id.index("R") + 1 : spot_id.index("C")])
            col = int(spot_id[spot_id.index("C") + 1 :])
            return floor, row, col
        except ValueError:
            return -1, -1, -1
