class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            slot = intervals[i]
            if ans[-1][1] >= slot[0]:
                ans[-1][1] = max(ans[-1][1], slot[1])
            else:
                ans.append(slot)
        return ans