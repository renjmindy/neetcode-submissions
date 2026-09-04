class Solution:
    def compress(self, chars: List[str]) -> int:
        
        r, ans = 0, 0

        while r < len(chars):
            cnt = 0
            cur = chars[r]
            while r < len(chars) and chars[r] == cur: cnt += 1; r += 1
            chars[ans] = cur; ans += 1
            if cnt > 1:
                for c in str(cnt): chars[ans] = c; ans += 1

        return ans
