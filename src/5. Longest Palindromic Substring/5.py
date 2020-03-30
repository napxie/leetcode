class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心算法
        size = len(s)
        if size < 2:
            return s
        max_len = 1
        res = s[0]
        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i+1)
            cur_max_sub = palindrome_odd if odd_len > even_len else palindrome_even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub
        return res

    def __center_spread(self, s, size, left, right):
        i, j = left, right
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j], j - i - 1

    def longestPalindrome1(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_len, start = 1, 0
        # for i in range(n): dp[i][i] = True
        for j in range(1, n):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len, start = cur_len, i
        return s[start:start+max_len]

    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        res = s[0]
        for i in range(n-1):
            for j in range(n):
                if j - i + 1 > max_len and self.__valid(s, i, j):
                    max_len = j - i + 1
                    res = s[i:j+1]
        return res

    def __valid(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    s = "babad"
    print(Solution().longestPalindrome(s))
    print(Solution().longestPalindrome1(s))
    print(Solution().longestPalindrome2(s))
