class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        Time = O(n)
        ans = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                if ans[0] == -1:
                    ans[0] = i
                ans[1] = i
        return ans
        '''
        start = 0
        end = len(nums)-1
        ans = [-1,-1]
        while start <= end:
            m = start + (end-start)//2
            if nums[m] == target: 
                if m==0 or nums[m-1] != target:
                    ans[0] = m
                    break
                else:
                    end = m-1
            elif nums[m] > target:
                end = m-1
            else:
                start = m+1
        start = 0
        end = len(nums)-1
        while start <= end:
            m = start + (end-start)//2
            if nums[m] == target: 
                if m==len(nums)-1 or nums[m+1] != target:
                    ans[1] = m
                    break
                else:
                    start = m+1
            elif nums[m] > target:
                end = m-1
            else:
                start = m+1
        return ans
if __name__ == "__main__":
    data = map(loads,stdin)
    f = open("user.out","w")
    while True:
        try:
            a = next(data)
            t = next(data)
            ans = Solution().searchRange(a,t)
            print(dumps(ans).replace(', ',','),file = f )
        except StopIteration:
            exit(0)