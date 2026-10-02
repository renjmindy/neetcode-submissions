class Solution:
    def isValid(self, s: str) -> bool:
        
        mp = {'(':')', '{':'}', '[':']'}
        ans = list()

        for c in s:
            if c in mp: ans.append(c)
            else:
                if not ans or mp[ans[-1]] != c: return False
                else: ans.pop()

        return len(ans) == 0