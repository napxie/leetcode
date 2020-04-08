from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j = 0, 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                j += 1
                i += 1
            else:
                j += 1
        return i


if __name__ == "__main__":
    g, s = [1, 2, 3], [1, 1]
    print(Solution().findContentChildren(g, s))
