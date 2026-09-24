# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        sums = []
        i, j = head, head

        while j:
            sums.append(i.val)
            i = i.next
            j = j.next.next
        
        k = -1
        while i:
            sums[k] += i.val
            i = i.next
            k -= 1
        
        return max(sums)