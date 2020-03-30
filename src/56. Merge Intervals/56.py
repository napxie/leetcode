from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for i in intervals:
            if not res or res[-1][-1] < i[0]:
                res.append(i)
            else:
                res[-1][-1] = max(i[1], res[-1][1])
        return res


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))
