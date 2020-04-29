# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None:
            return False
        if t2 == None:
            return True
        # find the root of t2 in t1
        return self.dfs(t1, t2) or self.checkSubTree(t1.left , t2) or self.checkSubTree(t1.right, t2)
    
    def dfs(self, t1, t2):
        # t2 is over
        if t2 == None:
            return True
        # t2 is not over and t1 is over
        elif t2 != None and t1 == None:
            return False
        # not equal
        elif t2.val != t1.val:
            return False
        # equal, then search left and right
        else:
            return self.dfs(t1.left, t2.left) and self.dfs(t1.right, t2.right)  # 注意这里是and
            
    def checkSubTree1(self, t1: TreeNode, t2: TreeNode) -> bool:
        def check(root, sub) -> bool:
            if not root:
                return False if sub else True
            if (root and not sub) or (root.val != sub.val):
                return False
            return check(root.left, sub.left) and check(root.right, sub.right)

        if not t1: return False
        if not t2: return True

        queue = [t1]
        while queue:
            next_queue = []
            while queue:
                node = queue.pop()
                if check(node, t2): 
                    return True
                if node.left: next_queue += [node.left]
                if node.right: next_queue += [node.right]
            queue = next_queue
        
        return False