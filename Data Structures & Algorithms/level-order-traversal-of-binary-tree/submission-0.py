# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = list()
        current = [root]
        nxt = list()
        while current:
            tmp = list()
            for n in current:
                if n is None:
                    continue
                tmp.append(n.val)
                nxt.append(n.left)
                nxt.append(n.right)
            if tmp:
                res.append(tmp)
            else:
                break
            current = nxt
            nxt = list()
        return res
        