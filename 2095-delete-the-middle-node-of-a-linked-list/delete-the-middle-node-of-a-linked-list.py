# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return None

        prev, i, j = None, head, head

        while j and j.next:
            prev, i, j = i, i.next, j.next.next
        
        prev.next = i.next
        return head
        