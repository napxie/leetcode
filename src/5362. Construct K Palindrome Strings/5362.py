class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        elif n == k:
            return True

        ans, odd = [0] * 26, 0
        for i in range(len(s)):
            ans[ord(s[i]) - 97] += 1
        for i in range(26):
            if ans[i] % 2 == 1:
                odd += 1
        return odd <= k

    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k and sum(map(lambda x: x % 2, Counter(s).values())) <= k
