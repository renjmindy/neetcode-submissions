class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        mp = Counter(text)

        return min(mp['b'] // 1, mp['a'] // 1, mp['l'] // 2, mp['o'] // 2, mp['n'] // 1)