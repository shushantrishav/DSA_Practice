# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Update diameter at this node
            self.diameter = max(self.diameter, left_height + right_height)

            # Return height to parent
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.diameter