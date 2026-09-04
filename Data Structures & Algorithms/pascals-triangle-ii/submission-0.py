class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ans = list()

        for i in range(rowIndex + 1):
            tmp = list()
            for j in range(i + 1):
                if j == 0 or j == i: tmp.append(1)
                else: tmp.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(tmp)

        return ans[rowIndex]