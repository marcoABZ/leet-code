# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        i, j, a1 = head, head.next, head.next
        while j and j.next:
            k, l = j.next, j.next.next
            i.next = k
            j.next = l
            i, j = k, l
        
        i.next = a1
        return head

        