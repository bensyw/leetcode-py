from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        # Similar to LC61
        # But here we don't use closure to define DFS
        # We use class method / clearing call stack techniques to get the number of num_of_solutions
        # Closure method would get unbounded local variable error
        diag1 = set()
        diag2 = set()
        used_cols = set()

        return self.dfs(n, diag1, diag2, used_cols, 0)

    def dfs(self, n, diag1, diag2, used_cols, row):
        if row == n:
            return 1

        num_of_solutions = 0

        for col in range(n):
            # Check if the placement is valid
            if (row + col not in diag1 and
                row - col not in diag2 and
                    col not in used_cols):

                # Add the diag1 diag2 and columns to the unavailable hashset
                diag1.add(row + col)
                diag2.add(row - col)
                used_cols.add(col)

                # Update the number of num_of_solutions
                num_of_solutions += self.dfs(n,
                                             diag1, diag2, used_cols, row + 1)

                # Clearing hashsets
                diag1.remove(row + col)
                diag2.remove(row - col)
                used_cols.remove(col)

        return num_of_solutions
