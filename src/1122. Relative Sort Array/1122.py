from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = [0 for _ in range(1001)]
        ans = []
        for i in range(len(arr1)):
            arr[arr1[i]] += 1
        for i in range(len(arr2)):
            while arr[arr2[i]] > 0:
                ans.append(arr2[i])
                arr[arr2[i]] -= 1
        for i in range(len(arr)):
            while arr[i] > 0:
                ans.append(i)
                arr[i] -= 1
        return ans


if __name__ == "__main__":
    arr1, arr2 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]
    print(Solution().relativeSortArray(arr1, arr2))
