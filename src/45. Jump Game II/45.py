from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        step, end, max_bound = 0, 0, 0
        for i in range(len(nums)-1):
            max_bound = max(max_bound, nums[i]+i)
            if i == end:
                 end = max_bound
                 step += 1
                 if end >= len(nums) - 1:
                     return step
        return step

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(Solution().jump(nums))