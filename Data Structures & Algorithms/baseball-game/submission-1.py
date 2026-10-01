class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        ans = list()

        for i, op in enumerate(operations):
            if op == '+': 
                ans.append(sum(ans[-2:]))
            elif op == 'C':
                ans.pop()
            elif op == 'D':
                ans.append(ans[-1]*2)
            else:
                ans.append(int(op))

        return sum(ans)