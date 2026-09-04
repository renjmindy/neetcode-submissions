class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        
        i, j, k = 0, 0, 0
        p, q, r = 0, 0, 0

        for xi, yi in zip(x, y):
            if xi == i: p = max(p, yi)
            elif xi == j: q = max(q, yi) 
            elif xi == k: r = max(r, yi)
            elif ((yi > p) or (yi > q) or (yi > r)): 
                mini = min(p, q, r) # minimal is 0
                if mini == p: i, p = xi, yi
                elif mini == q: j, q = xi, yi
                else: k, r = xi, yi
            print(i, j, k, p, q, r)

        return p + q + r if p > 0 and q > 0 and r > 0 else -1

        