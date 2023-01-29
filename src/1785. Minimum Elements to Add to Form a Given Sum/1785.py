class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return (abs(sum(nums)-goal) + limit -1 ) // limit
if __name__ == "__main__":
    print(Solution().minElements(nums, limit, goal))