from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]

if __name__ == "__main__":
    amount, coins = 5, [1, 2, 5]
    print(Solution().change(amount, coins))

