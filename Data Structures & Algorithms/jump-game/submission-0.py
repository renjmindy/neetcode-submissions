class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        ans = [0] * len(nums)
        ans[0] = nums[0]
        print(ans[0])

        for r in range(1, len(nums)):
            if ans[r - 1] < r: return False
            ans[r] = max(ans[r - 1], r + nums[r])
            print(ans[r])

        return ans[-1] >= len(nums) - 1