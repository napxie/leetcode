"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def traverse_node(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level+1)
        result = []
        if root is not None:
            traverse_node(root, 0)
        return result
;