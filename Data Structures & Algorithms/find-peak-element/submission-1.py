class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            pivot = l + (r - l) // 2
            if pivot > 0 and nums[pivot] < nums[pivot - 1]: r = pivot - 1
            elif pivot < len(nums) - 1 and nums[pivot] < nums[pivot + 1]: l = pivot + 1
            else: return pivot