# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkequal(root, subRoot):
            if root == None and subRoot == None:
                return True
            if (root == None or subRoot == None) or (root.val != subRoot.val):
                return False
            return checkequal(root.left, subRoot.left) and checkequal(root.right, subRoot.right)
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        if root.val == subRoot.val:
            if checkequal(root, subRoot):
                return True
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        return False
        