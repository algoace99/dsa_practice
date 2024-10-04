class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        '''
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
        '''
        # Using Sorting, without extra space
        skill.sort()
        n = len(skill)
        ans = 0
        req = skill[0] + skill[-1]

        for i in range(n//2):
            if skill[i] + skill[-i-1] != req:
                return -1
            ans += skill[i]*skill[-i-1]
        return ans