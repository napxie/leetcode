from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    res.append((i, j))
        for x in res:
            for i in range(m):
                if matrix[i][x[1]] != 0:
                    matrix[i][x[1]] = 0
            for i in range(n):
                if matrix[x[0]][i] != 0:
                    matrix[x[0]][i] = 0
        return matrix

    def setZeroes1(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for x in range(n):
                        if matrix[x][j] != 0:
                            matrix[x][j] = float('inf')
                    for y in range(m):
                        if matrix[i][y] != 0:
                            matrix[i][y] = float('inf')
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
        return matrix
