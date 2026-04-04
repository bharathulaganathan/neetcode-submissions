# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find_depth(node, depth):
            if node == None:
                return depth
            l = find_depth(node.left, depth+1)
            r = find_depth(node.right, depth+1)
            return max(l,r)
        return find_depth(root, 0)
        