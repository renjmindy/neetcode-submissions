class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = Counter(nums)

        ans = sorted(mp.items(), key = lambda x:x[1], reverse = True)[:k]

        #print(ans)

        return list(i[0] for i in ans)