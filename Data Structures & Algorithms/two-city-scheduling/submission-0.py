class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda x: x[0] - x[1])

        print(costs)

        ans = 0

        for r in range(len(costs)):
            if r < len(costs) // 2: ans += costs[r][0]
            else: ans += costs[r][1]

        return ans