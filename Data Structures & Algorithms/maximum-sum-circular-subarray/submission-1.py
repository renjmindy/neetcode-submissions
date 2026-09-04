class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        premax, ansmax, premin, ansmin = nums[0], nums[0], nums[0], nums[0]

        for r in range(1, len(nums)):
            premax = max(nums[r], premax + nums[r])
            ansmax = max(ansmax, premax)
            premin = min(nums[r], premin + nums[r])
            ansmin = min(ansmin, premin)

        return max(ansmax, sum(nums) - ansmin) if ansmax > 0 else ansmax 