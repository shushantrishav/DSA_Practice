# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preorder(root):
            if (root == None):
                return -1
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ans