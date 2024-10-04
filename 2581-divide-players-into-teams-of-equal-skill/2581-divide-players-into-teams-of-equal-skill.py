class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        tot = sum(skill)

        if tot % (len(skill)//2) != 0:
            return -1
        
        count = Counter(skill)

        req = tot//(len(skill)/2)

        sum_ans = 0
        for s in skill:
            if count[s] == 0:
                continue
            diff = req - s
            if count[diff] == 0:
                return -1
            sum_ans += s * diff
            count[s] -= 1
            count[diff] -= 1
        return int(sum_ans)