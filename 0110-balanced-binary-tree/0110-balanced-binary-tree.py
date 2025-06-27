# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0  # height of null is 0

            left_height = dfs(node.left)
            if left_height == -1:
                return -1  # propagate imbalance up

            right_height = dfs(node.right)
            if right_height == -1:
                return -1  # propagate imbalance up

            if abs(left_height - right_height) > 1:
                return -1  # imbalance detected

            return 1 + max(left_height, right_height)

        return dfs(root) != -1
