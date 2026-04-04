# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        heapq.heapify(arr)
        counter = count()
        for node in lists:
            while node:
                heapq.heappush(arr, (node.val, next(counter), node))
                node = node.next
        prev = ListNode()
        head = prev
        current = None
        while arr:
            current = heapq.heappop(arr)[2]
            prev.next = current
            prev = current
        return head.next