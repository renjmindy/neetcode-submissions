class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        mp = Counter(arr)
        mp_sort = dict(sorted(mp.items(), key = lambda x:x[1]))
        cnt = 0

        for element in arr:
            if element in mp_sort and mp_sort[element] == 1:    
                cnt += 1
                if cnt == k: return element

        return ""