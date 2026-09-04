class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        ans = [False] * len(s)

        ans[0] = True

        cnt = 0

        for r in range(1, len(s)):
            if r >= minJump and ans[r - minJump]: cnt += 1
            if r >= maxJump + 1 and ans[r - maxJump - 1]: cnt -= 1
            
            ans[r] = cnt > 0 and s[r] == '0'

        return ans[len(s) - 1]