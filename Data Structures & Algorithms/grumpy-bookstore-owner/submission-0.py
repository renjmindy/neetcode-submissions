class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0

        ans += sum( [customers[i] if grumpy[i] == 0 else 0 for i in range(len(customers))] )

        cnt = 0

        cnt += sum( [customers[i] if grumpy[i] == 1 else 0 for i in range(minutes)] )

        add = cnt

        for i in range(minutes, len(customers)):
            if grumpy[i - minutes] == 1: cnt -= customers[i - minutes]
            if grumpy[i] == 1: cnt += customers[i]

            add = max(add, cnt)

        return ans + add