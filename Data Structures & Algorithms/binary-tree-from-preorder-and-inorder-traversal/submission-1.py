# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node = TreeNode()
        node.val = preorder[0]
        root = inorder.index(node.val)
        if root != 0:
            node.left = self.buildTree(preorder[1:1+root], inorder[:root])
        if root + 1 != len(inorder):
            node.right = self.buildTree(preorder[root+1:], inorder[root+1:])
        return node
        