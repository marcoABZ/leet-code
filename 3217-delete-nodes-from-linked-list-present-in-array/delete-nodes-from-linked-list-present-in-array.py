# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev, curr = None, head
        nums = set(nums)

        while curr:
            if curr.val in nums:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return head