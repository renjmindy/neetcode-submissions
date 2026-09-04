class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            pivot = l + (r - l) // 2

            if nums[pivot] == target: return True
            
            elif nums[l] == nums[pivot]: l += 1; continue

            elif nums[l] < nums[pivot]:
                if nums[l] <= target < nums[pivot]: r = pivot - 1
                else: l = pivot + 1

            else:
                if nums[pivot] < target <= nums[r]: l = pivot + 1
                else: r = pivot - 1

        return False
