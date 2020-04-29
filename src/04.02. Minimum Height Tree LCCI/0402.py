# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        left, right = 0, len(nums) - 1
        if left > right:
            return None

        mid = (left + right) // 2
        root = TreeNode(nums[mid]) # 跟节点
        root.left = self.sortedArrayToBST(nums[:mid]) # 建立左子树
        root.right = self.sortedArrayToBST(nums[mid + 1:]) # 建立右子树
        return root