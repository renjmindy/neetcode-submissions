class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        ans = list()

        for log in logs:
            if log == "../":
                if ans: ans.pop()
            elif log != "./":
                ans.append(log)

        return len(ans)