class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        pre, ans = -math.inf, -math.inf

        for r in range(len(nums)):
            pre = max(nums[r], pre + nums[r])
            ans = max(ans, pre)

        return ans