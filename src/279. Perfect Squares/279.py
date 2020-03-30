import math


class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        dp = [float('inf')] * (n+1)
        # bottom case
        dp[0] = 0
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        return dp[-1]

    def numSquares1(self, n: int) -> int:
        from collections import deque
        if n == 0:
            return 0
        queue = deque([n])
        step = 0
        visited = set()
        while(queue):
            step += 1
            l = len(queue)
            for _ in range(l):
                tmp = queue.pop()
                for i in range(1, int(tmp**0.5)+1):
                    x = tmp-i**2
                    if(x == 0):
                        return step
                    if(x not in visited):
                        queue.appendleft(x)
                        visited.add(x)
        return step


if __name__ == "__main__":
    n = 12
    print(Solution().numSquares(n))
    print(Solution().numSquares1(n))
