class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        zeros, ones = s.count('0'), len(s) - s.count('0')

        return '1' * (ones - 1) + '0' * zeros + '1'