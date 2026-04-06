# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def find_max(node):
            right = find_max(node.right) if node.right else 0
            val = node.val
            left = find_max(node.left) if node.left else 0
            self.res = max(self.res, right+val, val, left+val, right+left+val)
            return max(right+val, val, left+val)
        find_max(root)
        return self.res
        