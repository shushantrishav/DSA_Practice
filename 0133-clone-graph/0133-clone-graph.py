"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clone_map = {}

        def dfs(curr_node):
            if curr_node in clone_map:
                return clone_map[curr_node]

            # Clone the current node
            copy = Node(curr_node.val)
            clone_map[curr_node] = copy

            # Clone neighbors recursively
            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        return dfs(node)