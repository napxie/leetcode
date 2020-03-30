class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row=0, count=0):
            for col in range(n):
                if not (rows[col] or hills[row-col] or dales[row+col]):
                    rows[col], hills[row-col], dales[row+col] = 1, 1, 1
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack(row+1, count)
                    rows[col],  hills[row-col], dales[row+col] = 0, 0, 0
            return count
        rows, hills, dales = [0] * n, [0]*(2*n-1), [0]*(2*n-1)
        return backtrack()


if __name__ == "__main__":
    n = 8
    print(Solution().totalNQueens(n))
