# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
        helper(root, 0)
        return levels


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
    print(Solution().levelOrder(treeRoot))
