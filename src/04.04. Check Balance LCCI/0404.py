# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 计算以当前节点为根的树深度
    def Depth(self, root: TreeNode) -> int:
        if root:
            return 1 + max(self.Depth(root.left), self.Depth(root.right))
        return 0


    def isBalanced(self, root: TreeNode) -> bool:
        # 空树是AVL
        if not root:
            return True
        # 若左右子树深度超过1，非AVL
        if abs(self.Depth(root.left) - self.Depth(root.right)) > 1:
            return False
        # 递归执行，当出现不满足AVL性质的子树时，执行短路运算立即返回结果
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced1(self, root: TreeNode) -> bool:
        def checkHeight(root):
            if not root: return -1

            leftHeight = checkHeight(root.left)
            if leftHeight == float('inf'): return float('inf') # 向上传递错误

            rightHeight = checkHeight(root.right)
            if rightHeight == float('inf'): return float('inf') # 向上传递错误

            heightDiff = leftHeight - rightHeight
            if abs(heightDiff) > 1:
                return float('inf') # 发现错误，把它传回来
            else:
                return max(leftHeight, rightHeight) + 1

        return checkHeight(root) != float('inf')