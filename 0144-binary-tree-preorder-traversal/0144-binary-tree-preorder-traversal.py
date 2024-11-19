# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Pre-Order - root, left, roght
        '''
        # Iterative Approach
        if root is None:
            return []

        ans = []
        s = [root]
        while s:
            temp = s.pop()
            ans.append(temp.val)
            if temp.right:
                s.append(temp.right)
            if temp.left:
                s.append(temp.left)
        return ans
        '''
        # Recursive Approach
        ans = []
        def pre_order(node):
            if node is None:
                return
            ans.append(node.val)
            pre_order(node.left)
            pre_order(node.right)
        
        pre_order(root)

        return ans