class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashed = {}
        for num in nums:
            hashed[num] = hashed.get(num,0) + 1
        max_heap = []
        heapq.heapify_max(max_heap)
        for key, val in hashed.items():
            heapq.heappush_max(max_heap, (val, key))
        res = []
        for _ in range(k):
            res.append(heapq.heappop_max(max_heap)[1])
        return res