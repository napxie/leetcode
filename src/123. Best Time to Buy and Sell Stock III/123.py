from typing import List
from os import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices: return 0
        # n = len(prices)
        # dp = [[[0]*2 for _ in range(3)] for _ in range(n)]
        # for i in range(3):
        #     dp[0][i][0], dp[0][i][1] = 0, -prices[0]
        # for i in range(1, n):
        #     for j in range(3):
        #         if not j:
        #             dp[i][j][0] = dp[i-1][j][0]
        #         else:
        #             dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])
        #         dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])
        # return dp[n-1][2][0]
        # return max(dp[n-1][0][0], dp[n-1][1][0], dp[n-1][2][0])

        if not prices: return 0
        n = len(prices)
        dp_i10, dp_i20, dp_i11, dp_i21 = 0, 0, -sys.maxsize - 1, -sys.maxsize - 1
        for i in range(n):
            dp_i20 = max(dp_i20, dp_i21 +  prices[i])
            dp_i21 = max(dp_i21, dp_i10 -  prices[i])
            dp_i10 = max(dp_i10, dp_i11 +  prices[i])
            dp_i11 = max(dp_i11, -prices[i])
        return dp_i20


if __name__ == "__main__":
    prices = [3,3,5,0,0,3,1,4]
    print(Solution().maxProfit(prices))