class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid + 1
                right -= 1
            elif target > nums[left]:
                right = mid - 1
                left += 1
            elif nums[left] > nums[mid]:
                right = mid - 1
                left += 1
            else:
                left = mid + 1
                right -= 1
        return -1


        