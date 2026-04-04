# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.val = list()
        def get_small(node):
            if node.left:
                get_small(node.left)
            self.val.append(node.val)
            if node.right:
                get_small(node.right)
            return
            if len(self.val) > k:
                return self.val[k-1]
        get_small(root)
        return self.val[k-1]
        