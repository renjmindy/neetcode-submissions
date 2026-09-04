class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)

        while l <= r:
            pivot = l + (r - l) // 2
            tot, cnt = 0, 1

            for weight in weights:
                if tot + weight <= pivot: tot += weight
                else: tot = weight; cnt += 1

            if cnt <= days: r = pivot - 1
            else: l = pivot + 1

        return l

