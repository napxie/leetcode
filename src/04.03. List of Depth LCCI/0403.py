# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        levels = []
        def dfs(node, level):
            if not node: return None
            if len(levels) == level:
                levels.append(ListNode(node.val))
            else:
                head = ListNode(node.val)
                head.next = levels[level]
                levels[level] = head
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
            return levels
        return dfs(tree, 0)