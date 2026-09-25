import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.not_in = set()

    def popSmallest(self):
        """
        :rtype: int
        """
        for i in range(1,1001):
            if i not in self.not_in:
                self.not_in.add(i)
                return i

        return None

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num in self.not_in:
            self.not_in.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)