from typing import List
from collections import deque


class Solution:
    # Improvement:
    # Use a queue, popleft() and appendleft() to only search for '.' once
    # Use check valid soduku in one iteration
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_hash_set = [set() for _ in range(9)]
        col_hash_set = [set() for _ in range(9)]
        box_hash_set = [set() for _ in range(9)]
        visit = deque()
        for row in range(9):
            for col in range(9):
                # Find all '.' to fill
                if board[row][col] == '.':
                    visit.append((row, col))
                # Add all filled slots to hashsets
                else:
                    row_hash_set[row].add(board[row][col])
                    col_hash_set[col].add(board[row][col])
                    box_hash_set[row//3 * 3 + col//3].add(board[row][col])

        def dfs():
            if not visit:
                return True
            row, col = visit.popleft()
            for num in map(str, range(1, 10)):
                # Validate soduku
                if ((num not in row_hash_set[row]) and
                    (num not in col_hash_set[col]) and
                        num not in box_hash_set[row//3 * 3 + col//3]):
                    # Add new num to hashsets
                    # Add new num to the board
                    board[row][col] = num
                    row_hash_set[row].add(board[row][col])
                    col_hash_set[col].add(board[row][col])
                    box_hash_set[row//3 * 3 + col//3].add(board[row][col])
                    if dfs():
                        return True
                    # Clear new num from the hashsets
                    # Clear new num from the board
                    row_hash_set[row].remove(board[row][col])
                    col_hash_set[col].remove(board[row][col])
                    box_hash_set[row//3 * 3 + col//3].remove(board[row][col])
                    board[row][col] = '.'
            visit.appendleft((row, col))
            return False

        dfs()
