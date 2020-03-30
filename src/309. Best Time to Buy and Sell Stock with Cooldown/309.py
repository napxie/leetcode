from typing import List
from os import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        if n == 1:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[-2][0], dp[-1][0], dp[-1][1] = 0, 0, -sys.maxsize - 1
        for i in range(n):
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        return dp[n-1][0]

    def maxProfit1(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        if n == 1:
            return 0
        dp_pre_0, dp_i_0, dp_i_1 = 0, 0, -sys.maxsize - 1
        for i in range(n):
            temp = dp_i_0
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_pre_0 = temp
        return dp_i_0


if __name__ == "__main__":
    prices = [1, 2, 3, 0, 2]
    print(Solution().maxProfit(prices))
