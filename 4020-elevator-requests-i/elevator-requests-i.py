class Solution(object):
    def elevatorRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[int]
        :rtype: int
        """
        curr = 0
        result = 0

        for req in requests:
            result += abs(req - curr)
            curr = req
        
        return result