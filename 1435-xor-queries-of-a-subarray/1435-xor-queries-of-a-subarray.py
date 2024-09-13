class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0]
        for i in arr:
            pre.append(pre[-1]^i)
        ans = []
        print(pre)
        for start, end in queries:
            ans.append(pre[end+1]^pre[start])
        return ans