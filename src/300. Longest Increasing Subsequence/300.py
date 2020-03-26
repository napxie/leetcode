from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i+j) // 2
                if tails[m] < num: 
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            if j == res: 
                res += 1
        return res
        
        # if not nums: return 0
        # dp = [1] *len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums))