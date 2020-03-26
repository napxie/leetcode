from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if i == j == 0: continue
        #         elif i == 0: grid[i][j] = grid[i][j-1] + grid[i][j]
        #         elif j == 0: grid[i][j] = grid[i-1][j] + grid[i][j]
        #         else: grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        # return grid[-1][-1]

        dp = [0] * (len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j == 0: dp[j] = dp[j] + grid[i][j]
                elif i == 0: dp[j] = dp[j-1] + grid[i][j]
                else: dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]
if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(Solution().minPathSum(grid))