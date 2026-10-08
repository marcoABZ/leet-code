# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB

        while a and b:
            if a == b:
                return a
            a = a.next
            b = b.next
        
        if not a:
            a = headB
        else:
            b = headA

        while a and b:
            if a == b:
                return a
            a = a.next
            b = b.next
        
        if not a:
            a = headB
        else:
            b = headA
        
        while a and b:
            if a == b:
                return a
            a = a.next
            b = b.next
        
        return None