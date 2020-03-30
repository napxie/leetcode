# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GRAY, node))
            else:
                res.append(node.val)
        return res

    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root: TreeNode) -> List[int]:
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

    def __init__(self):
        self.res = []

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        if root != None:
            self.res.append(root.val)
            self.preorderTraversal2(root.left)
            self.preorderTraversal2(root.right)

        return self.res


def createTree(root):
    if root == None:
        return root

    Root = TreeNode(root[0])
    nodeQueue = [Root]
    index = 1
    front = 0
    while index < len(root):
        node = nodeQueue[front]

        item = root[index]
        index += 1
        if item != None:
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(root):
            break

        item = root[index]
        index += 1
        if item != None:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)

        front += 1

    return Root


def printTree(root):
    if root != None:
        print(root.val)
        printTree(root.left)
        printTree(root.right)


if __name__ == "__main__":
    root = [1, None, 2, 3]
    treeRoot = createTree(root)
    printTree(treeRoot)
    print(Solution().preorderTraversal2(treeRoot))
    print(Solution().preorderTraversal(treeRoot))
    print(Solution().preorderTraversal1(treeRoot))
