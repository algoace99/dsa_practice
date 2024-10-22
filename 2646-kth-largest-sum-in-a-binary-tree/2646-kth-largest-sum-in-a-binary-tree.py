# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        temp = [root]
        current_sum = 0
        
        while temp:
            current_sum = sum([i.val for i in temp])
            heapq.heappush(res, current_sum)
            if len(res) > k:
                heapq.heappop(res)
            local_temp = []
            for i in temp:
                if i.left is not None:
                    local_temp.append(i.left)
                if i.right is not None:
                    local_temp.append(i.right)
            temp = local_temp
        return -1 if len(res) < k else res[0]
        '''
        res = []
        temp = [root]
        current_sum = 0
        
        while temp:
            current_sum = sum([i.val for i in temp])
            res.append(current_sum)
            local_temp = []
            for i in temp:
                if i.left is not None:
                    local_temp.append(i.left)
                if i.right is not None:
                    local_temp.append(i.right)
            temp = local_temp
        res.sort()
        return -1 if len(res) < k else res[-k]
        '''