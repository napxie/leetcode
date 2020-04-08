class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        queue, visited,  = [(0, 0, 0, 0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            if not 0 <= i < m or not 0 <= j < n or k < si + sj or (i, j) in visited:
                continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)

    def movingCount1(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if not 0 <= i < m or not 0 <= j < n or k < si + sj or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)

    def movingCount2(self, m: int, n: int, k: int) -> int:
        from collections import deque
        def addDigit(a, b):
            ans = 0
            while a != 0:
                ans += a % 10
                a //= 10
            while b != 0:
                ans += b % 10
                b //= 10
            return ans
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        matrix[0][0] = 1
        temp = deque()
        temp.append([0, 0])
        res = 0
        while temp:
            x, y = temp.popleft()
            res += 1
            for x_bias, y_bias in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_x, new_y = x + x_bias, y + y_bias
                if new_x < 0 or new_x > m - 1 or new_y < 0 or new_y > n - 1 or addDigit(new_x, new_y) > k or matrix[new_x][new_y] == 1:
                    continue
                matrix[new_x][new_y] = 1
                temp.append([new_x, new_y])
        return res


if __name__ == "__main__":
    m, n, k = 2, 3, 1
    print(Solution().movingCount(m, n, k))
    print(Solution().movingCount1(m, n, k))
    print(Solution().movingCount2(m, n, k))
