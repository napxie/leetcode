from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [0] * (amount+1)
        for i in range(1, amount+1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, res[i-c]+1)
                res[i] = cost
        if res[amount] == float('inf'):
            return -1
        else:
            return res[amount]


if __name__ == "__main__":
    coins, amount = [1, 2, 5], 11
    print(Solution().coinChange(coins, amount))
