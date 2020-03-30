from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
        output = []
        backtrack()
        return output


if __name__ == "__main__":
    n, k = 4, 2
    print(Solution().combine(n, k))
