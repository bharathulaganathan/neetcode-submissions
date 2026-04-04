# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = list()
        def addEle(node):
            if node is None:
                return
            addEle(node.left)
            self.res.append(node.val)
            addEle(node.right)
            return
        addEle(root)
        for i in range(len(self.res)-1):
            if self.res[i] >= self.res[i+1]:
                return False
        return True