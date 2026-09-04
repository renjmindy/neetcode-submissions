class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        l, r = 0, n 

        while l <= r:
            pivot = l + (r - l) // 2
            coins = (pivot * (pivot + 1)) // 2
            if coins == n: return pivot
            elif coins < n: l = pivot + 1
            else: r = pivot - 1

        return r