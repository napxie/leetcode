from collections import deque
from typing import List
import operator
import itertools


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 代码写法参考了官方题解
        R, C = len(board), len(board[0])
        # 状态压缩转化盘面数据, 二维->一维
        start = tuple(itertools.chain(*board))
        # 建立bfs辅助队列, 存储tuple(一维盘面, 0的位置, 操作步数)
        queue = deque([(start, start.index(0), 0)])
        # 存储已访问的状态
        visited = {start}
        # 设置终止目标
        target = tuple([*range(1, R*C)]+[0])
        while queue:
            board, posn, depth = queue.popleft()
            if operator.eq(board, target):
                return depth
            # 一维盘面进行遍历的四个方向为(-1, 1, -C, C)
            for d in (-1, 1, -C, C):
                nex = posn+d
                # 确保顶点的合法性(在盘面上)
                if abs(nex//C-posn//C)+abs(nex % C-posn % C) != 1:
                    continue
                if 0 <= nex < R*C:
                    nex_board = list(board)
                    # 交换位置/移动方格
                    nex_board[posn], nex_board[nex] = nex_board[nex], nex_board[posn]
                    nex_board = tuple(nex_board)
                    if nex_board not in visited:
                        visited.add(nex_board)
                        queue.append([nex_board, nex, depth+1])
        return -1


if __name__ == "__main__":
    board = [[1, 2, 3], [4, 0, 5]]
    print(Solution().slidingPuzzle(board))
