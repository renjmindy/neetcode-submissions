class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = list()

        intervals.append(newInterval)
        intervals.sort()

        ans.append(intervals[0])

        for r in range(1, len(intervals)):
            if ans[-1][1] >= intervals[r][0]:
                ans[-1][1] = max(ans[-1][1], intervals[r][1])
            else:
                ans.append(intervals[r])

        return ans 