from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row=0):
            for col in range(n):
                if not (cols[col] + hills[row-col] + dales[row+col]):
                    queens.add((row, col))
                    cols[col], hills[row-col], dales[row+col] = 1, 1, 1
                    if row + 1 == n:
                        solution = []
                        for _, col in sorted(queens):
                            solution.append('.'*col + 'Q' + '.'*(n-col-1))
                        output.append(solution)
                    else:
                        backtrack(row+1)
                    queens.remove((row, col))
                    cols[col], hills[row-col], dales[row+col] = 0, 0, 0
        cols, hills, dales = [0]*n, [0]*(2*n-1), [0]*(2*n-1)
        queens, output = set(), []
        backtrack()
        return output


if __name__ == "__main__":
    n = 4
    print(Solution().solveNQueens(n))
