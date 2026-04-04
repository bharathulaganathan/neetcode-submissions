# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = 0
        node = head
        while node:
            list_len += 1
            node = node.next
        target = list_len - n
        prev = None
        current = head
        nxt = head.next
        for _ in range(target):
            prev = current
            current = nxt
            nxt = nxt.next
        if prev:
            prev.next = nxt
        else:
            head = head.next
        return head