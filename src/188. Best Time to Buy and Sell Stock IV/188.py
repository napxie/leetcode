from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or not k:
            return 0
        n = len(prices)
        # 如果k大于数组长度的一半，则可以用贪心解决
        if k > n//2:
            return self.greedy(prices)
        # 动态规划
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]
        res = []
        # 设置初始状态
        for i in range(k+1):
            dp[0][i][0], dp[0][i][1] = 0, -prices[0]
        # 开始两层循环
        for i in range(1, n):
            for j in range(k+1):
                if not j:
                    dp[i][j][0] = dp[i-1][j][0]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1]
                                      [j-1][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])
        # 找到最大值
        for m in range(k+1):
            res.append(dp[n-1][m][0])
        return max(res)

    def greedy(self, prices: List[int]):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res


if __name__ == "__main__":
    prices, k = [2, 4, 1], 2
    print(Solution().maxProfit(k, prices))
