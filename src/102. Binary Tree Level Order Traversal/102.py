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
        return helper(root, 0)

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root, ])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # go to next level
            level += 1

        return levels

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if len(levels) == level:
                levels.append([])
            if node.right:
                stack.append((node.right, level+1))
            levels[level].append(node.val)
            if node.left:
                stack.append((node.left, level+1))
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
