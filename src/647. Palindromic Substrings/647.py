class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for center in range(2*n-1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

        if not s:
            return 0
        res = len(s)
        dp = [[i, i+1] for i in range(len(s))]
        for i in range(1, len(s)):
            for j in dp[i-1]:
                if j - 1 >= 0 and s[j-1] == s[i]:
                    res += 1
                    dp[i].append(j-1)
        return res


if __name__ == "__main__":
    s = "abc"
    print(Solution().countSubstrings(s))
