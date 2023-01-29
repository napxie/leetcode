from itertools import groupby


class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        for k, g in groupby(s):
            n = len(list(g))
            res += (n + 1) * n // 2
        return res % (10 ** 9 + 7)

if __name__ == "__main__":
    s = "abbcccaa"
    print(Solution().countHomogenous(s))