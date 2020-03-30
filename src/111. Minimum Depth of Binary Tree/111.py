# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root), ], float('inf')
            while stack:
                depth, root = stack.pop()
                children = [root.left, root.right]
                if not any(children):
                    min_depth = min(depth, min_depth)
                for c in children:
                    if c:
                        stack.append((depth+1, c))
        return min_depth

    def minDepth1(self, root: TreeNode) -> int:
        if not root:
            return 0
        children = [root.left, root.right]
        if not any(children):
            return 1
        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1
