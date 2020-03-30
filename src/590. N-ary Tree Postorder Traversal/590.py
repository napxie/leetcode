"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            stack.extend(root.children)
            # for c in root.children:
            #     stack.append(c)
        return output[::-1]
