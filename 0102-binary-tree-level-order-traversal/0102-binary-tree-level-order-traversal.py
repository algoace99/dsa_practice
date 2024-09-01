# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        current=[root]
        next=[]
        ans=[]
        while len(current)>0:
            ele=[]
            for i in current:
                ele.append(i.val)
                if i.left is not None:
                    next.append(i.left)
                if i.right is not None:
                    next.append(i.right)
            ans.append(ele)
            current=next
            next=[]
        return ans