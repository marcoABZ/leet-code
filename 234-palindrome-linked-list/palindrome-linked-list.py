# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        i, j = head, head
        while j and j.next:
            i = i.next
            j = j.next.next
        
        if j:
            i = i.next
        prev = None
        while i:
            nxt = i.next
            i.next, prev = prev, i
            i = nxt
        
        i, j = head, prev
        while i and j:
            if i.val != j.val:
                return False
            i = i.next
            j = j.next
        
        return True