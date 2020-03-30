# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        hashMap = {}

        def dfs(node, depth):
            if not node:
                return
            else:
                if depth not in hashMap:
                    hashMap[depth] = node.val
                else:
                    hashMap[depth] = max(node.val, hashMap[depth])
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 1)
        return [hashMap[i] for i in hashMap]
