from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i-stack[-1]-1)*heights[tmp])
            stack.append(i)
        return res
    def largestRectangleArea1(self, heights: List[int]) -> int:
        stack, res = [-1], 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                tmp = stack.pop()
                res = max(res, (i-stack[-1]-1)*heights[tmp])
            stack.append(i)
        return res


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea(heights))
    print(Solution().largestRectangleArea1(heights))
