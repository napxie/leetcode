from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        for i in range(m):
            if matrix[i][n-1] < target:
                i += 1
                continue
            if matrix[i][0] > target:
                return False
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                value = matrix[i][mid]
                if target == value:
                    return True
                else:
                    if target < value:
                        right = mid - 1
                    else:
                        left = mid + 1
        return False


if __name__ == "__main__":
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(Solution().findNumberIn2DArray(matrix))
