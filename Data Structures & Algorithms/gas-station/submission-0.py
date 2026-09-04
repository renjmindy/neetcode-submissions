class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) - sum(cost) < 0: return -1

        l, ans = 0, 0

        for r in range(len(gas)):
            ans += gas[r] - cost[r]

            if ans < 0:
                l = r + 1
                ans = 0

        return l