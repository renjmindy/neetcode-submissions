class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        ans = list()

        intervals.sort()
        ans.append(intervals[0])

        for r in range(1, len(intervals)):
            if ans[-1][1] > intervals[r][0]:
                ans[-1][1] = min(ans[-1][1], intervals[r][1])
            else:
                ans.append(intervals[r])

        print(ans)

        return len(intervals) - len(ans)