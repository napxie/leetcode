from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
        output = []
        n = len(nums)
        for k in range(n+1):
            backtrack()
        return output

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j+1, tmp+[nums[j]])
        helper(0, [])
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
    print(Solution().subsets1(nums))
