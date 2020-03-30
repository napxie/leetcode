from typing import List
from os import sys


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[-1][0], dp[-1][1] = 0, -sys.maxsize - 1
        for i in range(n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
        return dp[n-1][0]

    def maxProfit1(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp_i_0,  dp_i_1 = 0, -sys.maxsize - 1
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i] - fee)
        return dp_i_0


if __name__ == "__main__":
    prices, fee = [1, 3, 2, 8, 4, 9], 2
    print(Solution().maxProfit(prices, fee))
    print(Solution().maxProfit1(prices, fee))
