class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 0

        mums = list(set(nums))
        mums.sort()

        l, ans = 0, 0

        for r in range(1, len(mums)):
            if mums[r] - mums[r - 1] == 1: l += 1
            else:
                ans = max(ans, l + 1)
                l = 0

        ans = max(ans, l + 1)
        return ans



