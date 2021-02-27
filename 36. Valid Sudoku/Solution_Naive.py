from typing import List


class Solution:
    # Naive Approach: Check all three rules seperately
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rule 1: Row without repetition
        for row in board:
            hash_set = set()
            for ele in row:
                if ele == '.':
                    continue
                else:
                    if ele in hash_set:
                        return False
                    else:
                        hash_set.add(ele)
        # Rule 2: Col without repetition
        for x in range(0, 9):
            hash_set = set()
            for y in range(0, 9):
                ele = board[y][x]
                if ele == '.':
                    continue
                else:
                    if ele in hash_set:
                        return False
                    else:
                        hash_set.add(ele)
        # Rule 3: Sub-box without repetition
        # Get 9 sub-boxes
        for box_x in range(0, 3):
            for box_y in range(0, 3):
                hash_set = set()
                # Get all elements in the sub-box
                for x in range(3 * box_x, 3 * (box_x + 1)):
                    for y in range(3 * box_y, 3 * (box_y + 1)):
                        ele = board[y][x]
                        if ele == '.':
                            continue
                        else:
                            if ele in hash_set:
                                return False
                            else:
                                hash_set.add(ele)
        return True
