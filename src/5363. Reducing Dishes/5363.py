from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction, reverse=True)
        re, s = 0, 0
        for i, v in enumerate(satisfaction):
            s += v
            if s < 0:
                break
            re += s
        return re


if __name__ == "__main__":
    satisfaction = [-1, -8, 0, 5, -9]
    pritn(Solution().maxSatisfaction(satisfaction))
