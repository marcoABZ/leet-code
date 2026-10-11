class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        fs = set(friends)
        result = []

        for n in order:
            if n in fs:
                result.append(n)
        
        return result
