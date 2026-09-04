class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        ans = list()

        for l in range(len(arr) - 1):
            maxVal = max(arr[l+1:])
            ans.append(maxVal)

        ans.append(-1)

        return ans

        