class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        l, cnt, ans = 0, 0, 0
        nums.sort()

        for r in range(len(nums)):
            target = nums[r]
            cnt += nums[r]
            while ( (r - l + 1) * target ) - cnt > k:
                cnt -= nums[l]
                l += 1

            ans = max(ans, r - l + 1)

        return ans