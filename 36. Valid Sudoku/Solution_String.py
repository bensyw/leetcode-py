from typing import List


class Solution:
    # String Approach: Use a string in the hashset to improve readability
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(0, 9):
            for j in range(0, 9):
                number = board[i][j]
                if (number != '.'):
                    rule_row = number + ' in row ' + str(i)
                    rule_col = number + ' in col ' + str(j)
                    rule_box = number + ' in box ' + \
                        str(i // 3) + '-' + str(j // 3)
                    if (rule_row in seen or rule_col in seen or rule_box in seen):
                        return False
                    seen.add(rule_row)
                    seen.add(rule_col)
                    seen.add(rule_box)
        return True
