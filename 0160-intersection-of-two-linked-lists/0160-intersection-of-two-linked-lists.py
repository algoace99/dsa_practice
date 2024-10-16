# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        s = set()
        temp = headA
        while temp:
            s.add(temp)
            temp = temp.next
        temp = headB
        while temp:
            if temp in s:
                return temp
            temp = temp.next
        return None
        '''
        len_a = 0
        temp = headA
        while temp:
            len_a += 1
            temp = temp.next
        
        len_b = 0
        temp = headB
        while temp:
            len_b += 1
            temp = temp.next
        
        temp_1 = headA
        temp_2 = headB

        diff = len_a - len_b
        if diff > 0:
            while diff:
                temp_1 = temp_1.next
                diff -= 1
        else:
            diff = abs(diff)
            while diff:
                temp_2 = temp_2.next
                diff -= 1
        
        while temp_1 and temp_2:
            if temp_1 == temp_2:
                return temp_1
            temp_1 = temp_1.next
            temp_2 = temp_2.next
        
        return None