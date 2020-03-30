from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                return res
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                if j - i > 1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, len(nums)-1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif target < nums[i] + nums[j] + nums[l] + nums[r]:
                        r -= 1
                    else:
                        l += 1
        return res


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums, target))
