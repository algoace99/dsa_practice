class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        intervals.append(newInterval)
        intervals.sort(key = lambda a:a[0])
        ans = []
        for i in intervals:
            if len(ans)==0 or ans[-1][-1]<i[0]:
                ans.append(i)
            else:
                ans[-1][-1] = max(ans[-1][-1], i[1])
        return ans
        '''
        ans = []
        inserted = False 
        for i in intervals:
            if i[1] < newInterval[0]:
                ans.append(i)
            elif i[0] > newInterval[1]:
                if not inserted:
                    ans.append(newInterval)
                    inserted = True
                ans.append(i)
            else:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
        if not inserted:
            ans.append(newInterval)
        return ans