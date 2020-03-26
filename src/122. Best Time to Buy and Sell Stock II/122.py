from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not n: return 0
        dp = [[0]*2 for _ in range(n)]
        dp[-1][0], dp[-1][1] = 0, float('-inf')
        for i in range(n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]

    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)
        if not n: return 0
        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0

    def maxProfit2(self, prices: List[int]) -> int:
        maxprices = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxprices += prices[i] - prices[i-1]
        return maxprices
        
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))
    print(Solution().maxProfit1(prices))
    print(Solution().maxProfit2(prices))