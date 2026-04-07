class MedianFinder:

    def __init__(self):
        self.left = list()
        self.right = list()
        heapq.heapify_max(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        if len(self.right) == 0:
            heapq.heappush(self.right, num)
        elif num < self.right[0]:
            heapq.heappush_max(self.left, num)
            if len(self.left) - len(self.right) > 1:
                val = heapq.heappop_max(self.left)
                heapq.heappush(self.right, val)
        else:
            heapq.heappush(self.right, num)
            if len(self.right) - len(self.left) > 1:
                val = heapq.heappop(self.right)
                heapq.heappush_max(self.left, val)


    def findMedian(self) -> float:
        if len(self.left) < len(self.right):
            return self.right[0]
        elif len(self.left) > len(self.right):
            return self.left[0]
        else:
            return (self.right[0] + self.left[0])/2

        