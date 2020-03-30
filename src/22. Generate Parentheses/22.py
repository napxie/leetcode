from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.list = []
        self._gen(0, 0, n, "")
        return self.list

    def _gen(self, left, right, n, result):
        if left == right == n:
            return self.list.append(result)
        if left < n:
            self._gen(left+1, right, n, result+"(")
        if left > right and right < n:
            self._gen(left, right+1, n, result+")")

    def generateParenthesis1(self, n: int) -> List[str]:
        if n == 0:
            return []
        dp = [None for _ in range(n + 1)]
        dp[0] = [""]
        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                for s1 in left:
                    for s2 in right:
                        cur.append("(" + s1 + ")" + s2)
            dp[i] = cur
        return dp[n]


if __name__ == "__main__":
    n = 3
    print(Solution().generateParenthesis(n))
    print(Solution().generateParenthesis1(n))
