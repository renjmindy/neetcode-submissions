class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1: return 0

        l, cnt, ans = 0, 1, 0

        for r in range(len(nums)):
            cnt *= nums[r]
            while cnt >= k:
                cnt //= nums[l]
                l += 1
            ans += (r - l + 1)

        return ans