# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                # Find rightmost node in left subtree
                pre = root.left
                while pre.right:
                    pre = pre.right
                # Rewire connections
                pre.right = root.right
                root.right = root.left
                root.left = None
            # Move to next right node
            root = root.right