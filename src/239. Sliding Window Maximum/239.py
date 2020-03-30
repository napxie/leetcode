from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        win, res = [], []
        for i, num in enumerate(nums):
            if i >= k and win[0] == i - k:
                win.pop(0)
            while win and nums[win[-1]] <= num:
                win.pop()
            win.append(i)
            if i >= k - 1:
                res.append(nums[win[0]])
        return res


if __name__ == "__main__":
    nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    print(Solution().maxSlidingWindow(nums, k))
