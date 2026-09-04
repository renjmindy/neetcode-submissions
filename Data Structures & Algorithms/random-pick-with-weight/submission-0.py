class Solution:

    def __init__(self, w: List[int]):
        self.running_sum = list()
        tot = 0

        for i in w: tot += i; self.running_sum.append(tot)

        self.total = tot

    def pickIndex(self) -> int:

        target = random.randint(1, self.total)

        l, r = 0, len(self.running_sum) - 1

        while l <= r:
            pivot = l + (r - l) // 2
            if self.running_sum[pivot] < target: l = pivot + 1
            elif self.running_sum[pivot] > target: r = pivot - 1
            else: return pivot

        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()