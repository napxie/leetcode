from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0
        for i, jump in enumerate(nums):
            if max_i >= i and i + jump > max_i:
                max_i = i + jump
        return max_i >= i
    
if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(Solution().canJump(nums))