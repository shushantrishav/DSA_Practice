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

        max_width = 0
        queue = deque()
        queue.append((root, 0))  # (node, position)

        while queue:
            level_size = len(queue)
            _, first_pos = queue[0]  # position of first node at this level
            for _ in range(level_size):
                node, pos = queue.popleft()
                # Normalize pos relative to first_pos at this level
                norm_pos = pos - first_pos

                if node.left:
                    queue.append((node.left, 2 * norm_pos))
                if node.right:
                    queue.append((node.right, 2 * norm_pos + 1))
            # Compute width using positions relative to first_pos
            last_pos = norm_pos  # norm_pos from last node processed at this level
            max_width = max(max_width, last_pos + 1)

        return max_width