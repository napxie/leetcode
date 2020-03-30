import collections
from typing import List


class Solution:
    def __init__(self):
        self.directions = directions = [
            (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        i, j = click[0], click[1]
        if board[i][j] == "M":
            board[i][j] = "X"
        q = collections.deque()
        q.append(click)
        visited = set(click)

        def numBombs(board, i, j):
            mine_count = 0
            for d in self.directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                    mine_count += 1
            return mine_count
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                if board[x][y] == 'E':
                    bombsNextTo = numBombs(board, x, y)
                    board[x][y] = "B" if bombsNextTo == 0 else str(bombsNextTo)
                    if bombsNextTo == 0:
                        for d in self.directions:
                            ni, nj = x + d[0], y + d[1]
                            if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                                q.append((ni, nj))
                                visited.add((ni, nj))
        return board


if __name__ == "__main__":
    board = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"],
             ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]]
    click = [3, 0]
    print(Solution().updateBoard(board, click))
