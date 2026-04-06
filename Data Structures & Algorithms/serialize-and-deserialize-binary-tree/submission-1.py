# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = list()
        nodes = deque()
        nodes.append(root)
        while nodes:
            node = nodes.popleft()
            if not node:
                res.append("null")
            else:
                res.append(node.val)
                nodes.append(node.left)
                nodes.append(node.right)
        data = ""
        for d in res:
            data += str(d) + ","
        return data[:-1] if data else ""

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        data = data.split(",")
        data = deque(data)
        nodes = deque()
        node = data.popleft()
        root = TreeNode(val=node)
        nodes.append(root)
        while data:
            node = nodes.popleft()
            node.left = TreeNode(val=data.popleft())
            node.right = TreeNode(val=data.popleft())
            nodes.append(node.left)
            nodes.append(node.right)
        return root
