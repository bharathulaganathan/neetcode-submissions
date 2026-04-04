# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        while head:
            arr.append(head)
            head = head.next
        if len(arr) < 2:
            return
        i = 0
        last = None
        while i < len(arr)//2:
            if last:
                last.next = arr[i]
            arr[i].next = arr[-(i+1)]
            last = arr[-(i+1)]
            i += 1
        if len(arr) % 2 == 0:
            last.next = None
        else:
            last.next = arr[i]
            arr[i].next = None