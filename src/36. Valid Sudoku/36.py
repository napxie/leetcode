from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, columns, boxes = [{} for _ in range(9)], [{} for _ in range(9)], [
            {} for _ in range(9)]
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != '.':
                    box = (row//3)*3 + col//3
                    rows[row][num], columns[col][num], boxes[box][num] = rows[row].get(
                        num, 0) + 1, columns[col].get(num, 0) + 1, boxes[box].get(num, 0) + 1
                    if rows[row][num] > 1 or columns[col][num] > 1 or boxes[box][num] > 1:
                        return False
        return True


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                          ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().isValidSudoku(board))
