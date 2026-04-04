# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = list()
        node = head
        while node:
            current.append(node)
            node = node.next
        index = len(current) - 1
        while index > 0:
            node = current[index]
            node.next = current[index-1]
            index -= 1
        current[0].next = None
        return current[-1]