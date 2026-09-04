class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        ans = -1

        for r in range(len(nums)):
            if sum(nums[:r]) == sum(nums[r+1:]): ans = r; break

        return ans