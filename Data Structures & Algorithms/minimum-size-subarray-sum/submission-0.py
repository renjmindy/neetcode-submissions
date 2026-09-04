class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target: return 0

        l, cnt, ans = 0, 0, math.inf

        for r in range(len(nums)):
            cnt += nums[r]
            while cnt >= target:
                ans = min(ans, r - l + 1)
                cnt -= nums[l]
                l += 1

        return ans 