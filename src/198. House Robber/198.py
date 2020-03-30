from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        a = [[0]*2 for _ in range(n)]
        for i in range(n):
            a[i][0] = max(a[i-1][0], a[i-1][1])
            a[i][1] = a[i-1][0] + nums[i]
        return max(a[n-1][0], a[n-1][1])

    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        a = [0 for _ in range(n)]
        a[0] = nums[0]
        a[1] = max(nums[0], nums[1])
        res = float('-inf')
        for i in range(2, n):
            a[i] = max(a[i-1], a[i-2] + nums[i])
            res = max(res, a[i])
        return res

    def rob2(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))
