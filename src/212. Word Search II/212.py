from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, trie, s):
            c = board[i][j]
            if c not in trie:
                return
            trie = trie[c]
            if "end" in trie and trie["end"] == 1:
                res.append(s + c)
                trie["end"] = 0
            board[i][j] = "#"
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                new_i = x + i
                new_j = y + j
                if 0 <= new_i < row and 0 <= new_j < col and board[new_i][new_j] != "#":
                    dfs(new_i, new_j, trie, s + c)
            board[i][j] = c
        trie = {}
        for word in words:
            t = trie
            for w in word:
                t = t.setdefault(w, {})
            t["end"] = 1
        res = []
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                dfs(i, j, trie, "")
        return res


if __name__ == "__main__":
    words = ["oath", "pea", "eat", "rain"]
    board = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]
    print(Solution().findWords(board, words))
