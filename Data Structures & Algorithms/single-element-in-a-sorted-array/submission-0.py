class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            pivot = l + (r - l) // 2
            
            if (pivot == 0 and nums[pivot] != nums[pivot + 1]) or (pivot == len(nums) - 1 and nums[pivot] != nums[pivot] - 1) or (nums[pivot] != nums[pivot + 1] and nums[pivot] != nums[pivot - 1]): return nums[pivot]

            if pivot % 2:
                if nums[pivot - 1] == nums[pivot]: l = pivot + 1
                else: r = pivot - 1
            else:
                if nums[pivot - 1] == nums[pivot]: r = pivot - 1
                else: l = pivot + 1


        return nums[l]