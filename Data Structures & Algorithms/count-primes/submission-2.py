class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2: return 0

        ans = [1] * n
        ans[0], ans[1] = 0, 0

        for i in range(2, n):
            if ans[i]:
                ans[i**2:n:i] = ((n - 1 - i**2) // i + 1) * [0]

        return sum(ans)
        
        