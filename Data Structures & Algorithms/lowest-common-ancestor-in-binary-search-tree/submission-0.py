# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findNode(node, parents, target):
            if node is None:
                return None
            parents = parents.copy()
            parents.append(node)
            if node.val == target:
                return parents
            left = findNode(node.left, parents, target)
            right = findNode(node.right, parents, target)
            if left:
                return left
            elif right:
                return right
            else:
                return None
        p_arr = findNode(root, [], p.val)
        q_arr = findNode(root, [], q.val)
        i = min(len(p_arr), len(q_arr)) - 1
        while True:
            if p_arr[i] == q_arr[i]:
                return p_arr[i]
            i -= 1
        