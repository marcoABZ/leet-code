"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        st = []
        curr = head

        while curr:
            if curr.child:
                if curr.next:
                    st.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                child = curr.child
                curr.child = None
                curr = child
                continue
            if curr.next:
                curr = curr.next
                continue
            if st:
                node = st.pop()
                curr.next = node
                node.prev = curr
                curr = node
            else:
                break
        
        return head