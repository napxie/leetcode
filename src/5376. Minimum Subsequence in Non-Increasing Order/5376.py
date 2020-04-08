from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        if len(nums) <= 1:
            return nums
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return [nums[0]]
            else:
                return nums
        l, r = 1, len(nums) - 2
        print(l, r)
        left_max, right_max = nums[0], nums[len(nums) - 1]
        print(left_max, right_max)
        while l <= r:
            if right_max + nums[r] < left_max:
                right_max = right_max + nums[r]
                r -= 1
            else:
                left_max = left_max + nums[l]
                l += 1
        return nums[:l]


if __name__ == "__main__":
    nums = [8, 6, 9, 10, 11, 1111]
    print(Solution().minSubsequence(nums))
