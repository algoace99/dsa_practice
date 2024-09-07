# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        
        def dfs(node: Optional[TreeNode], current: Optional[ListNode]) -> bool:
            if not current:
                return True 
            if not node:
                return False
            if node.val != current.val:
                return False
            return dfs(node.left, current.next) or dfs(node.right, current.next)
        def traverse(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            if dfs(node, head):
                return True

            return traverse(node.left) or traverse(node.right)

        return traverse(root)