from typing import List


class Solution:
    def __init__(self):
        self.directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.__search_word(board, word, 0, i, j, marked, m, n):
                    return True
        return False

    def __search_word(self, board, word, index, start_x, start_y, marked, m, n):
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]
        if board[start_x][start_y] == word[index]:
            marked[start_x][start_y] = True
            for direction in self.directions:
                new_x, new_y = start_x + direction[0], start_y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n and not marked[new_x][new_y] and self.__search_word(board, word, index+1, new_x, new_y, marked, m, n):
                    return True
            marked[start_x][start_y] = False
        return False


if __name__ == "__main__":
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    print(Solution().exist(board))
