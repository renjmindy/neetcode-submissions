class CountSquares:

    def __init__(self):
        self.mp = defaultdict(int)
        self.np = list()

    def add(self, point: List[int]) -> None:
        self.mp[tuple(point)] += 1
        self.np.append(point)

    def count(self, point: List[int]) -> int:
        ans = 0
        px, py = point

        for x, y in self.np:
            if (abs(px - x) == abs(py - y)) and (px != x and py != y):
                ans += self.mp[(px, y)] * self.mp[(x, py)]

        return ans
