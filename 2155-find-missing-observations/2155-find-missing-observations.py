class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        lr=len(rolls) #length of rolls list
        total_sum = mean*(lr+n)
        req_sum = total_sum-sum(rolls)

        if req_sum > n*6 or req_sum < n:
            return []

        ans = [1]*n

        req_sum -= n
        index = 0


        while req_sum > 0:
            dice = min(req_sum,6-ans[index])
            ans[index] += dice
            req_sum -= dice
            index += 1
        return ans
