class Solution:
    def maxDifference(self, s: str) -> int:
        
        mp = Counter(s)
        mp_sort = sorted(mp.items(), key = lambda x:x[1])

        odd, even = list(), list()

        for k, v in mp_sort:
            if v % 2: odd.append(v)
            else: even.append(v)

        return max(odd) - min(even)