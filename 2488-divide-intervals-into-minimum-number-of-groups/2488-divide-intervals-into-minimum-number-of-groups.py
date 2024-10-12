class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        i,j = 0,0
        min_groups = 0
        curr_groups = 0
        while i < len(start):
            if start[i] <= end[j]:
                i += 1
                curr_groups += 1
            else:
                j += 1
                curr_groups -= 1
            min_groups = max(min_groups, curr_groups)
        return min_groups