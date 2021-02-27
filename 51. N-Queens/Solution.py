from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Append encoded solution to solutions
        # Solution encoding
        # solution  = [1, 3, 0, 2]
        # idx = row
        # val = col
        solutions = []

        def DFS(placed_queens, xy_dif, xy_sum):
            # num_placed_queens is the index of row
            num_placed_queens = len(placed_queens)
            if num_placed_queens == n:
                solutions.append(placed_queens)
                return None
            for col in range(n):
                # num_placed_queens is also the current row
                # col is the current col that we are trying to place a new queen
                # xy_dif is the diagonal 1
                # xy_sum is the diagonal 2
                # The next if-statement check if the placement is valid
                if (col not in placed_queens and
                    num_placed_queens - col not in xy_dif and
                        num_placed_queens + col not in xy_sum):
                    # Place the new queen.
                    # Record the occupied row, col, diag1, and diag2
                    # Note that we don't have to clear the call stack, since we are passing a new variable down at the recursive call.
                    DFS(placed_queens + [col],
                        xy_dif + [num_placed_queens - col],
                        xy_sum + [num_placed_queens + col])
        DFS([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in solution] for solution in solutions]
