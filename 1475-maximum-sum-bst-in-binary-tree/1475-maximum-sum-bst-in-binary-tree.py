# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        
        def postorder(node):
            if not node:
                return (True, float('inf'), float('-inf'), 0)  # isBST, min, max, sum
            
            left_isBST, left_min, left_max, left_sum = postorder(node.left)
            right_isBST, right_min, right_max, right_sum = postorder(node.right)
            
            # Check if current node is BST
            if left_isBST and right_isBST and left_max < node.val < right_min:
                curr_sum = node.val + left_sum + right_sum
                self.max_sum = max(self.max_sum, curr_sum)
                return (True, 
                        min(left_min, node.val),
                        max(right_max, node.val),
                        curr_sum)
            else:
                return (False, 0, 0, 0)
        
        postorder(root)
        return self.max_sum