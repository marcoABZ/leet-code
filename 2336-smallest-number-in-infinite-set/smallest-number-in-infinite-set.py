import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.current = 1
        self.not_in_s = set()
        self.not_in = []

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.not_in:
            val = heapq.heappop(self.not_in)
            self.not_in_s.add(val)
            return val

        self.current += 1
        self.not_in_s.add(self.current - 1)
        return self.current - 1

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num in self.not_in_s:
            self.not_in_s.remove(num)
            heapq.heappush(self.not_in, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)