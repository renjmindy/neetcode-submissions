class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            pivot = l + (r - l) // 2
            time = sum([math.ceil(banana * 1.0 / pivot) for banana in piles])

            if time <= h: ans = pivot; r = pivot - 1
            else: l = pivot + 1

        return ans