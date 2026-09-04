class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        premax, ansmax, premin, ansmin = 0, -math.inf, 0, math.inf

        for r in range(len(nums)):
            premax = max(nums[r], premax + nums[r])
            ansmax = max(ansmax, premax)
            premin = min(nums[r], premin + nums[r])
            ansmin = min(ansmin, premin)

        return max(ansmax, sum(nums) - ansmin) if ansmax > 0 else ansmax 