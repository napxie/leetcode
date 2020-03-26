from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    matrix[i][j] = 1
                    if i == 0 or j == 0:
                        res = max(matrix[i][j], res)
                    else:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
                        res = max(matrix[i][j], res)
                else:
                    matrix[i][j] = 0
        return res**2

if __name__ == "__main__":
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(Solution().maximalSquare(matrix))