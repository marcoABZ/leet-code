# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        i, j = head, head.next
        while j and j.next:
            if j == i:
                return True
            
            i = i.next
            j = j.next.next
        
        return False