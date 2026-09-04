class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        p, q = len(word), len(abbr)

        r1, r2 = 0, 0

        while r1 < p and r2 < q:
            if abbr[r2] == '0': return False
            if word[r1] == abbr[r2]: r1 += 1; r2 += 1
            elif abbr[r2].isalpha(): return False
            else:
                size = 0
                while r2 < q and abbr[r2].isdigit():
                    size = size * 10 + int(abbr[r2])
                    r2 += 1
                r1 += size

        return r1 == p and r2 == q