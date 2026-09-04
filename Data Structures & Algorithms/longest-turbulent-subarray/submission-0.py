class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        cnt, ans = 0, 0

        for r in range(len(arr)):
            if r >= 2 and (arr[r - 2] < arr[r - 1] > arr[r] or arr[r - 2] > arr[r - 1] < arr[r]): cnt += 1
            elif r >= 1 and arr[r - 1] != arr[r]: cnt = 2
            else: cnt = 1

            ans = max(ans, cnt)

        return ans