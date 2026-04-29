"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        ori_arr = dict()
        ori_q = [node]
        while ori_q:
            cur = ori_q.pop()
            nei = list()
            for n in cur.neighbors:
                if n.val not in ori_arr:
                    ori_q.append(n)
                nei.append(n.val)
            ori_arr[cur.val] = nei
        dup_arr = [Node() for _ in range(len(ori_arr))]
        for i, n in enumerate(dup_arr):
            n.val = i+1
            n.neighbors = list()
            for nei in ori_arr[i+1]:
                n.neighbors.append(dup_arr[nei-1])
        return dup_arr[0]