class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: return False

        n = ''

        while x > 0:

            n += str(x % 10)

            x //= 10

        return n == n[::-1]