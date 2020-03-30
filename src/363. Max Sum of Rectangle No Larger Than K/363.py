from sortedcontainers import SortedList
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n_row, n_col = len(matrix), len(matrix[0])
        ans = float('-inf')
        for l in range(n_col):
            sums = [0] * n_row
            for r in range(l, n_col):
                for i in range(n_row):
                    sums[i] += matrix[i][r]
                ans = max(ans, self.maxSubArray(sums, k))
        return ans

    def maxSubArray(self, nums, k):
        cur_sum, max_sum = 0, float('-inf')
        sums = [0]
        for i, n in enumerate(nums, 1):
            cur_sum += n
            idx = bisect.bisect_left(sums, cur_sum - k)
            if idx != i:
                max_sum = max(max_sum, cur_sum - sums[idx])
            bisect.insort(sums, cur_sum)
        return max_sum


if __name__ == "__main__":
    matrix, k = [[1, 0, 1], [0, -2, 3]], 2
    print(Solution().maxSumSubmatrix(map, k))
