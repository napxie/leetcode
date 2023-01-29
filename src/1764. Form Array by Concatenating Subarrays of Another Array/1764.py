from typing import List
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        k = 0
        for g in groups:
            while k + len(g) <= len(nums):
                if nums[k: k + len(g)] == g:
                    k += len(g)
                    break
                k += 1
            else:
                return False
        return True

if __name__ == '__main__':
    groups = [[1,-1,-1],[3,-2,0]]
    nums = [1,-1,0,1,-1,-1,3,-2,0]
    print(Solution().canChoose(groups, nums))
    