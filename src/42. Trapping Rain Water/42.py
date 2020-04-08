from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = [0] * (n + 1), [0] * (n + 1)
        ans = 0
        for i in range(1, len(height) + 1):
            l[i] = max(l[i - 1], height[i - 1])
        for i in range(len(height) - 1, 0, -1):
            r[i] = max(r[i + 1], height[i])
        for i in range(len(height)):
            ans += max(0, min(l[i + 1], r[i]) - height[i])
        return ans

    def trap1(self, height: List[int]) -> int:
        n = len(height)
        res, idx, stack = 0, 0, []
        while idx < n:
            while len(stack) > 0  and height[idx] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                h = min(height[idx], height[stack[-1]]) - height[top]
                w = idx - stack[-1] - 1
                res += h * w
            stack.append(idx)
            idx += 1
        return res

if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))
    print(Solution().trap1(height))
