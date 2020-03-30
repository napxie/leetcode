from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 0, None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate


if __name__ == "__main__":
    nums = [3, 2, 3]
    print(Solution().majorityElement(nums))
