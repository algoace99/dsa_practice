class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        l=[]
        for i in timePoints:
            hh, mm = i.split(':')
            m = int(hh)*60 + int(mm)
            l.append(m)
        l.sort()
        diff = []
        for i in range(1,len(l)):
            diff.append(l[i]-l[i-1])
        diff.append(24*60-l[-1]+l[0])
        return min(diff)