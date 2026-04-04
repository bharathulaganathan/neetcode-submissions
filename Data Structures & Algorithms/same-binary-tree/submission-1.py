# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_arr = [p]
        q_arr = [q]
        while p_arr and q_arr:
            p = p_arr.pop()
            q = q_arr.pop()
            if p == None and q == None:
                continue
            if p == None or q == None:
                return False
            if p.val != q.val:
                return False
            p_arr.extend([p.left, p.right])
            q_arr.extend([q.left, q.right])
        if p or q:
            return False
        return True