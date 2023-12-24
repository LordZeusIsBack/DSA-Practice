from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row
        for row in board:
            if not self.is_valid_set(row):
                return False

        # Check each column
        for col in zip(*board):
            if not self.is_valid_set(col):
                return False

        # Check each 3x3 sub-box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_valid_set(sub_box):
                    return False

        return True

    def is_valid_set(self, group: List[str]) -> bool:
        seen = set()
        for digit in group:
            if digit != '.':
                if digit in seen:
                    return False
                seen.add(digit)
        return True
