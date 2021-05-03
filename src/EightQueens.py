"""The n queens puzzle"""


class NQueens:
    """Generate all valid solutions for the n queens puzzle"""

    def __init__(self, size = 4, debug = False, positions: list = []):
        # Store the puzzle (problem) size and the number of valid solutions
        self.__size = size
        self.__solutions = 0

        if positions == []:
            self.positions = [-1] * self.__size
        elif len(positions) != self.__size:
            raise Exception("Length of positions passed must be equal to board size")
        else:
            self.positions = positions

        self.debug = debug
        self.board_text = ''

    def SetSize(self, new_size: int):
        self.__size = new_size
        self.__solutions = 0

    def GenerateSolutions(self):
        """Solve the n queens puzzle and print the number of solutions"""
        self.PutQueen(self.positions, 0)  
        return self.__solutions

    def PutQueen(self, positions, target_row):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the function calls itself trying to place a queen
        on the next row until all N queens are placed on the NxN board.
        """

        # Base (stop) case - all N rows are occupied
        if target_row == self.__size:
            if self.debug:
                self.DisplayBoard(positions)
            self.AddToBoardText(positions)
            self.__solutions += 1
        else:
            # For all N columns positions try to place a queen
            for column in range(self.__size):
                # Reject all invalid positions
                if self.ValidatePosition(positions, target_row, column):
                    positions[target_row] = column
                    self.PutQueen(positions, target_row + 1)

    def ValidatePosition(self, positions, ocuppied_rows, column):
        """
        Check if a given position is under attack from any of
        the previously placed queens (check column and diagonal positions)
        """
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                    positions[i] - i == column - ocuppied_rows or \
                    positions[i] + i == column + ocuppied_rows:

                return False
        return True

    def DisplayBoard(self, positions):
        """Show the full NxN board"""
        for row in range(self.__size):
            line = ""
            for column in range(self.__size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def AddToBoardText(self, positions):
        """Get textual representation of the NxN board"""
        for row in range(self.__size):
            for column in range(self.__size):
                if positions[row] == column:
                    self.board_text += "Q "
                else:
                    self.board_text += ". "
            self.board_text += "\n\n\n"
        self.board_text += "\n\r"
        self.board_text += ("-" * self.__size) + "\n"

