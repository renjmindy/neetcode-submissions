class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or len(s) <= numRows: return s

        ans = [[] for _ in range(numRows)]
        idx, inc = 0, 1

        for c in s:
            ans[idx] += c
            if idx == 0: inc = 1
            elif idx == numRows - 1: inc = -1
            idx += inc

        for i in range(numRows):
            ans[i] = ''.join(ans[i])            

        return ''.join(ans)