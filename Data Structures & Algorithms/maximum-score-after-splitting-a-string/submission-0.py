class Solution:
    def maxScore(self, s: str) -> int:
        
        ones, zeroes, ans = list(), list(), list()

        for i in range(len(s) - 1):
            mp = dict(Counter(s[:i + 1]))
            if '0' in mp: ones.append(mp['0'])
            else: ones.append(0)
            np = dict(Counter(s[i + 1:]))
            if '1' in np: zeroes.append(np['1'])
            else: zeroes.append(0)

        for i in range(len(ones)):
            ans.append(ones[i] + zeroes[i])

        return max(ans)
                