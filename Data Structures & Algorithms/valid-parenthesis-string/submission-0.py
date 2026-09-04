class Solution:
    def checkValidString(self, s: str) -> bool:
        
        sopen, sstar = list(), list()

        for i, c in enumerate(s):
            if c == '(': sopen.append(i)
            elif c == '*': sstar.append(i)
            else:
                if sopen: sopen.pop()
                elif sstar: sstar.pop()
                else: return False    

        while sopen and sstar:
            if sopen[-1] > sstar[-1]: return False
            else:
                sopen.pop()
                sstar.pop()

        return len(sopen) == 0 