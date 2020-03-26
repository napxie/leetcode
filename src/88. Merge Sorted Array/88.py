from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m - 1, n - 1, m + n - 1 
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2+1] = nums2[:p2+1]

if __name__ == "__main__":
    nums1, nums2, m, n = [1,2,3,0,0,0], [2,5,6], 3, 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)