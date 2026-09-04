class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        tot = sum(arr[:k])
        ans = 0
        if tot / k >= threshold: ans += 1

        for i in range(k, len(arr)):
            tot -= arr[i - k]
            tot += arr[i]
            if tot / k >= threshold: ans += 1

        return ans