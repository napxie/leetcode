from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]


if __name__ == "__main__":
    nums = [2, 3, 2]
    print(Solution().rob(nums))
