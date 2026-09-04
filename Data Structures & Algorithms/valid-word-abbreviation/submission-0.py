class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        p, q = len(word), len(abbr)

        l = r = 0

        while l < p and r < q:
            if abbr[r] == '0': return False
            if word[l] == abbr[r]: l += 1; r += 1
            elif abbr[r].isalpha(): return False
            else:
                size = 0
                while r < q and abbr[r].isdigit():
                    size  = size * 10 + int(abbr[r])
                    r += 1
                l += size

        return l == p and r == q