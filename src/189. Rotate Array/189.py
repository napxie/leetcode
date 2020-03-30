from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        return nums

    def reverse(self, nums: List[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate1(self, nums: List[int], k: int) -> None:
        count, index, temp = 0, 0, nums[0]
        done_index = [0]
        while count < len(nums):
            count, target = count+1, (index+k) % len(nums)
            temp, nums[target] = nums[target], temp
            if target not in done_index:
                index = target
            elif target + 1 < len(nums):
                index, temp = target + 1, nums[target + 1]
            done_index.append(index)


if __name__ == "__main__":
    nums, k = [1, 2, 3, 4, 5, 6, 7], 3
    Solution().rotate(nums, k)
    print(nums)
