class Solution:
    def reverse(self, x: int) -> int:
        
        sign = 1 if x >= 0 else -1
        x = abs(x)
        ans = 0

        while x:

            ans = ans * 10 + x % 10
            x //= 10

        ans *= sign

        return ans if 2**31 - 1 > ans > -(2**31) else 0