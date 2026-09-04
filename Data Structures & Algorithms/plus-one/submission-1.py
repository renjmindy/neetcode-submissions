class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = [str(digit) for digit in digits]

        n = int(''.join(s))

        n = n + 1

        sp = str(n)

        return [int(c) for c in sp]