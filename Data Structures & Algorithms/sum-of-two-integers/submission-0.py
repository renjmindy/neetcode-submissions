class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask, maxi = 0xFFFFFFFF, 0x7FFFFFFF

        x = a & mask
        y = b & mask

        while y:
            carry = (x & y) << 1
            x = x ^ y
            y = carry & mask

        return x if x <= maxi else ~(x ^ mask)