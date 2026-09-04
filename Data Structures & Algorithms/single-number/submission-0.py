class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        mums = Counter(nums)

        for k, v in mums.items():
            if v == 1: return k

        return -1
        