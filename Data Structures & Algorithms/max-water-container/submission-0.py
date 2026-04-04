class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        j = 0
        k = len(heights) - 1
        while j < k:
            current = min(heights[j], heights[k]) * (k - j)
            water = max(water, current)
            if heights[j] > heights[k]:
                k -= 1
            else:
                j += 1
        return water