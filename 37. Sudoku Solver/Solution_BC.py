from typing import List


class Solution:
    # Naive backtracking approach that is highly readable
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

    def findUnassigned(self):
        """
        Find the unassigned slot
        """
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1

    def getRange(self, x):
        """
        Get the range for a box
        """
        x -= x % 3
        return range(x, x + 3)

    def isSafe(self, row, col, choice):
        """
        Check if the choice makes a valid Soduku board
        """
        isRowSafe = all(self.board[row][_] != choice for _ in range(9))
        isColSafe = all(self.board[_][col] != choice for _ in range(9))
        isBoxSafe = all(self.board[box_row][box_col] != choice
                        for box_row in self.getRange(row)
                        for box_col in self.getRange(col))
        return isRowSafe and isColSafe and isBoxSafe

    def solve(self):
        """
        Recursive function that places a choice in the next unassigned slot
        """
        row, col = self.findUnassigned()
        if (row, col) == (-1, -1):
            return True  # No more unassigned slot

        # Use map to convert number 1~9 to string
        for num in map(str, range(1, 10)):
            if self.isSafe(row, col, num):
                self.board[row][col] = num  # Place a safe choice
                # Call a recursive function to place the next choice
                if self.solve():
                    return True  # Base condition: All solved
                # Trick: Clear the choices when exiting the recursive stack
                self.board[row][col] = '.'
