class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        mp = Counter(arr)
        ans = list()

        for k, v in mp.items():
            if k == v: ans.append(k)

        return max(ans) if ans else -1