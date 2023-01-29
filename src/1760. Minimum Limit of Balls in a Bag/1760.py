from typing import List
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right, ans = 1, max(nums), 0
        
        while left <= right:
            y = (left + right) // 2
            ops = 0
            for x in nums:
                ops += ((x - 1) // y)

            # ops = sum((x - 1) // y for x in nums)
            if ops <= maxOperations:
                ans = y
                right = y - 1
            else:
                left = y + 1
        return ans
if __name__ == "__main__":
    nums = [2,4,8,2]
    maxOperations = 4
    print(Solution().minimumSize(nums, maxOperations))
