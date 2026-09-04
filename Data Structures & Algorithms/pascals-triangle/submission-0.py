class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = list()

        for i in range(numRows):
            tmp = list()
            for j in range(i + 1):
                if j == 0 or j == i: tmp.append(1)
                else:
                    tmp.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(tmp)

        return ans