from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def could_place(d, row, col):
            return not (d in rows[row] or d in columns[col] or d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            rows[row][d], columns[col][d], boxes[box_index(
                row, col)][d] = rows[row][d]+1, columns[col][d]+1, boxes[box_index(row, col)][d] + 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            del rows[row][d], columns[col][d], boxes[box_index(row, col)][d]
            board[row][col] = '.'

        def place_next_numbers(row, col):
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            if board[row][col] == '.':
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
        n = 3
        N = n * n
        def box_index(row, col): return (row // n) * n + col // n
        rows, columns, boxes = [defaultdict(int) for i in range(N)], [defaultdict(
            int) for i in range(N)], [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)
        sudoku_solved = False
        backtrack()
        return board


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".",
                                                                                                                                                                                              "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().solveSudoku(board))
