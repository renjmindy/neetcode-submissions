class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        r, d = list(), list()

        for i, s in enumerate(senate):
            if s == 'R': r.append(i)
            else: d.append(i)

        while r and d:
            r1 = r[0]
            d1 = d[0]
            r.pop(0)
            d.pop(0)
            if r1 < d1: r.append(len(senate) + r1)
            else: d.append(len(senate) + d1)

        return "Radiant" if len(r) > len(d) else "Dire"