class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = [(value, timestamp)]
        else:
            self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ans = ""

        if key not in self.mp: return ans

        pairs = self.mp.get(key, [])

        if len(pairs) == 1 and pairs[0][1] <= timestamp: return pairs[0][0]

        if timestamp < self.mp[key][0][1]: return ans

        l, r = 0, len(pairs) - 1

        while l <= r:
            pivot = l + (r - l) // 2
            if pairs[pivot][1] > timestamp: r = pivot - 1
            else: ans = pairs[pivot][0]; l = pivot + 1

        return ans

        
