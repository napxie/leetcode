# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

    def invertTree1(self, root: TreeNode) -> TreeNode:
        stack, cur = [], root
        while stack or cur:
            while cur:
                cur.left, cur.right = cur.right, cur.left
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        return root
