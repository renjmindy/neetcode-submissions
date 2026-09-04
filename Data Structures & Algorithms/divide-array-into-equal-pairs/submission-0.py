class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        mp = Counter(nums)

        for k, v in mp.items():
            if v % 2: return False

        return True