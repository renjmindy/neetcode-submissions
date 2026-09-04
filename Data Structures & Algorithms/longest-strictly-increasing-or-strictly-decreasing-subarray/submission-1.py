class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        p, m, ans = 1, 1, 0

        for r in range(1, len(nums)):
            if nums[r] > nums[r - 1]: p += 1; m = 1
            elif nums[r] < nums[r - 1]: p = 1; m += 1
            else: p = 1; m = 1

            ans = max(ans, p, m)

        return ans if len(nums) > 1 else 1