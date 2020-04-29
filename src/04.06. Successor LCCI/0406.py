# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        flag, ans = False, None
        def f(r):
            nonlocal flag, ans
            if r and not ans:
                f(r.left)
                if flag:
                    ans = r
                    flag = False
                if r is p:
                    flag = True
                f(r.right)
        f(root)
        return ans