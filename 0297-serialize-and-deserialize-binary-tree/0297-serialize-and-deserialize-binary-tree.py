# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if not node:
                vals.append('null')
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        vals = []
        preorder(root)
        return ','.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build():
            val = next(vals)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        vals = iter(data.split(','))
        return build()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))