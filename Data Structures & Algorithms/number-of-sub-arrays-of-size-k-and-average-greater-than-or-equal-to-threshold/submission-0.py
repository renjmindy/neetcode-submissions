class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        l, tot, ans = 0, 0, 0

        for r in range(len(arr)):
            tot += arr[r]
            while r - l + 1 >= k:
                if tot / (r - l + 1) >= threshold: ans += 1
                tot -= arr[l]
                l += 1

        return ans 