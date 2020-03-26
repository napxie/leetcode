from functools import lru_cache
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        def code(r, c):
            return 1 << (r * C + c)
        def neiors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc
        target = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val % 2 == 0:
                    target |= code(r, c)

                if val == 1:
                    sr, sc = r, c
                if val == 2:
                    tr, tc = r, c

        @lru_cache(None)
        def dp(r, c, todo):
            if r == tr and c == tc:
                return +(todo == 0)
            ans = 0
            for nr, nc in neiors(r, c):
                if todo & code(nr, nc):
                    ans += dp(nr, nc, todo ^ code(nr, nc))
            return ans

        return dp(sr, sc, target)

if __name__ == "__main__":
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    print(Solution().uniquePathsIII(grid))