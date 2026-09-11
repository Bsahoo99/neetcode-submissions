# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inverse(node):
            if node is None:
                return None

            node.left, node.right = node.right, node.left
            inverse(node.left)
            inverse(node.right)

            return node

        return inverse(root)        