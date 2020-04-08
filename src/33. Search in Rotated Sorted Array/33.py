from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        left, right = 0, len(nums) - 1             
        while True:
            if left == right:
                return left if nums[left] == target else -1
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1


if __name__ == "__main__":
    nums, target = [4, 5, 6, 7, 0, 1, 2], 3
    print(Solution().search(nums,  target))
    nums, target = [4, 5, 6, 7, 0, 1, 2], 0
    print(Solution().search(nums,  target))
