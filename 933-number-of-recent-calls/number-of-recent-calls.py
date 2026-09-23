class RecentCounter(object):

    def __init__(self):
        self.times = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.times.append(t)
        i = 0
        while self.times[i] + 3000 < t:
            i += 1
        self.times = self.times[i:]
        return len(self.times)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)