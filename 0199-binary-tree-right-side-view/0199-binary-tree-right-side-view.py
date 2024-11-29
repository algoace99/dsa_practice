# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l  = [root]
        ans = []

        while l:
            temp = l
            internal = []
            buk = []
            for i in temp:
                if i:
                    buk.append(i.val)
                    if i.left:
                        internal.append(i.left)
                    if i.right:
                        internal.append(i.right)
            if len(buk) > 0:
                ans.append(buk[-1])
            l = internal
        return ans