class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        sSum = sum([ord(x) for x in s])
        tSum = sum([ord(y) for y in t])

        return chr(tSum - sSum)