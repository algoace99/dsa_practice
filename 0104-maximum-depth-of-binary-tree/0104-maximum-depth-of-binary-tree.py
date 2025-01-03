# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        # Iterative, Level Order Traversal
        if root is None:
            return 0
        
        depth = 0
        level = [root]
        while level:
            depth += 1
            temp = []
            for i in level:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            level = temp
        return depth
        '''
        # Recursive
        if root is None: 
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))