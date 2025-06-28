# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [float('-inf')]

        def cb(node, ans):
            if not node:
                return 0
            lsum = max(0, cb(node.left, ans))
            rsum = max(0, cb(node.right, ans))
            ans[0] = max(ans[0], lsum + rsum + node.val)
            return node.val + max(lsum, rsum)

        cb(root, ans)
        return ans[0]