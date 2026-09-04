class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l, r = 0, num

        while l <= r:
            pivot = l + (r - l) // 2
            if pivot ** 2 == num: return True
            elif pivot ** 2 > num: r = pivot - 1
            else: l = pivot + 1

        return False