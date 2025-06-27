# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_width = 0
        first_pos_per_level = {}

        def dfs(node, level, pos):
            if not node:
                return

            # Record first position seen at this level
            if level not in first_pos_per_level:
                first_pos_per_level[level] = pos

            current_width = pos - first_pos_per_level[level] + 1
            self.max_width = max(self.max_width, current_width)

            dfs(node.left, level + 1, 2 * pos)
            dfs(node.right, level + 1, 2 * pos + 1)

        dfs(root, 0, 0)
        return self.max_width