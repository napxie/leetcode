class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for _ in range(n)]
        for i in range(m):
            dp[0][i] = 1
        for i in range(n):
            dp[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def uniquePaths1(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))


if __name__ == "__main__":
    m, n = 3, 2
    print(Solution().uniquePaths(3, 2))
