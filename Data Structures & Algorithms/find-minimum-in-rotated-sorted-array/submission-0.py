class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            pivot = l + (r - l) // 2

            if nums[pivot] < nums[(pivot - 1 + len(nums)) % len(nums)] and nums[pivot] < nums[(pivot + 1) % len(nums)]: return nums[pivot]
            elif nums[pivot] < nums[r]: r = pivot - 1
            else: l = pivot + 1

        return nums[0]