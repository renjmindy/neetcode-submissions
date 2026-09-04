class Solution:

    def encode(self, strs: List[str]) -> str:
        
        return ''.join(str(len(stri)) + '/' + stri for stri in strs)

    def decode(self, s: str) -> List[str]:

        i, ans = 0, list()

        while i < len(s):
            j = i
            while s[j] != '/': j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j

        return ans
