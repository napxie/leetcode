from typing import List
from os import sys


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, imax, imin = -sys.maxsize - 1, 1, 1
        for i in range(len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])
            imin = max(imin * nums[i], nums[i])
            res = max(res, imax)
        return res


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print(Solution().maxProduct(nums))
