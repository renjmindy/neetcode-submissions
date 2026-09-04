class Solution:
    def helper(self, nums: List[int], p: int, pivot: int) -> bool:

        l, cnt = 0, 0

        while l < len(nums) - 1 and cnt < p:
            if nums[l + 1] - nums[l] <= pivot: cnt += 1; l += 2
            else: l += 1

        return cnt >= p

    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()

        l, r = 0, max(nums) - min(nums)

        while l <= r:
            pivot = l + (r - l) // 2
            if self.helper(nums, p, pivot): r = pivot - 1
            else: l = pivot + 1

        return l
