class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sn, pn = len(s), len(p)
        dp = [[False] * (pn+1) for _ in range(sn+1)]
        dp[0][0] = True
        for j in range(1, pn+1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j-1]
        for i in range(1, sn+1):
            for j in range(1, pn+1):
                if (s[i-1] == p[j-1] or p[j-1] == "?"):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]


if __name__ == "__main__":
    s, p = "aa", "a"
    print(Solution().isMatch(s, p))
