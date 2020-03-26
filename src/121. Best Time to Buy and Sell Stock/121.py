from typing import List
from os import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1 
        # n = len(prices)
        # if not n: return 0
        # dp = [[0]*2 for _ in range(n)]
        # dp[-1][0], dp[-1][1] = 0, -sys.maxsize - 1
        # for i in range(n):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #     dp[i][1] = max(dp[i-1][1], -prices[i])
        # return dp[n-1][0]
        
        # 2
        n = len(prices)
        if not n: return 0
        dp = [[0]*2 for _ in range(n)]
        dp_i_0, dp_i_1 = 0, -sys.maxsize - 1
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))