# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # {hd: [(level, value)]}
        node_map = defaultdict(list)

        def dfs(node, hd, level):
            if not node:
                return
            node_map[hd].append((level, node.val))

            dfs(node.left, hd - 1, level + 1)
            dfs(node.right, hd + 1, level + 1)

        dfs(root, 0, 0)

        result = []
        for hd in sorted(node_map):
            col_nodes = sorted(node_map[hd])  # sorted by level, then value
            col_values = [val for lvl, val in col_nodes]
            result.append(col_values)

        return result