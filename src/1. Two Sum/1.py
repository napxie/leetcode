from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target-num], i]
            dic[num] = i


if __name__ == "__main__":
    nums, target = [2, 7, 11, 15], 9
