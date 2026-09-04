class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        mp, np = list(pattern), s.split(' ')

        return len(set(mp)) == len(set(np)) == len(set(zip(mp, np))) if len(mp) == len(np) else False