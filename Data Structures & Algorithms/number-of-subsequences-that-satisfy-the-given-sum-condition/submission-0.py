class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        mod = 10 ** 9 + 7

        ans = 0

        l, r = 0, len(nums) - 1

        nums.sort()

        while l <= r:
            if nums[l] + nums[r] > target: r -= 1
            else:
                ans += 2**(r - l)
                ans %= mod
                l += 1

        return ans

        