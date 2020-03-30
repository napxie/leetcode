from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        # 找位置i左边最大值
        for i in range(1, n):
            max_left[i] = max(height[i], max_left[i-1])
        # 找位置i右边最大值
        for i in range(n-2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1])
        print(max_left)
        print(max_right)
        # 求结果
        res = 0
        for i in range(n):
            res += min(max_left[i], max_right[i]) - height[i]
        return res


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))
