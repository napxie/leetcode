from typing import List


class Solution:
    def minMutation1(self, start: str, end: str, bank: List[str]) -> int:
        def toNumber(gene):
            table = {v: i for i, v in enumerate('ATGC')}
            return sum(table[g] * 1 << (2 * i) for i, g in enumerate(gene))
        bank = set(map(toNumber, bank))
        start = toNumber(start)
        end = toNumber(end)
        queue = [(start, 0)]
        viset = set([start])
        while queue:
            gene, step = queue.pop(0)
            if gene == end:
                return step
            for x in range(8):
                for y in range(4):
                    next = gene ^ (y << (x * 2))
                    if next in bank and next not in viset:
                        viset.add(next)
                        queue.append((next, step + 1))
        return -1

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 广度优先搜索
        bank = set(bank)  # 转换为set, in判断只需O(1)时间
        if end not in bank:  # 目标不可行，直接返回-1
            return -1
        q = [(start, 0)]  # 初始结点以及当前步数
        change = {'A': 'TCG', 'T': 'ACG',
                  'C': 'ATG', 'G': 'ATC'}  # 每个基因对应的可变换基因
        while q:  # 用队列实现广度优先
            node, step = q.pop(0)
            if node == end:  # 已经到达目标
                return step
            for i, v in enumerate(node):  # 当前序列的每一个基因
                for j in change[v]:  # 该基因可以改变的方式
                    new = node[:i]+j+node[i+1:]  # 改变后的序列
                    if new in bank:  # 如果该序列可行
                        q.append((new, step+1))  # 入队，继续广度搜索
                        bank.remove(new)  # 避免重复遍历
        return -1  # 队列空了说明不可达


if __name__ == "__main__":
    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(Solution().minMutation(start, end, bank))
    print(Solution().minMutation1(start, end, bank))
