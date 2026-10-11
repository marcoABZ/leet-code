class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """
        space = 100000
        index = -1

        for i, cap in enumerate(capacity):
            if cap == itemSize:
                return i
            elif cap > itemSize:
                if cap - itemSize < space:
                    space = cap - itemSize
                    index = i
        
        return index