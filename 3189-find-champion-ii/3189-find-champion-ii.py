class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        d = {}
        for i in range(n):
            d[i] = 0
        for i in edges:
            d[i[1]] += 1
        champion  = []
        for i in range(n):
            if d[i] == 0:
                champion.append(i)
        return -1 if len(champion) > 1 else champion[0]
             