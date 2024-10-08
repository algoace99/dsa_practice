class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        #Brute force solution:
        #generate all combinations and check
        #Time : O(n)
        #Space: O(1)

        max_count=0
        for i in range(len(nums)):
            zeros=0
            for j in range(i,len(nums)):
                if nums[j]==0: zeros+=1
                if zeros<=k:
                    max_count=max(max_count,j-i+1)
                else:
                    break
        return max_count
        '''
        #Time: O(n)
        #Space: O(1)
        max_w=0
        l=0
        zeros=0
        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1
            while zeros > k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            max_w=max(max_w,r-l+1)
        return max_w