from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            sums, cnt = 0, 1
            for i in nums:
                if sums + i > mid:
                    cnt += 1
                    sums = i
                else:
                    sums += i
            if cnt <= m:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    nums = [7, 2, 5, 10, 8]
    m = 2
    print(Solution().splitArray(nums, m))
