class TimeMap(object):

    def __init__(self):
        self.storage = dict()

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self.storage:
            self.storage[key].append((timestamp, value))
        else:
            self.storage[key] = [(timestamp, value)]

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.storage:
            return ""
        
        values = self.storage[key]
        i, j = 0, len(values) - 1
        best = None

        while i <= j:
            mid = i + (j - i) // 2

            if values[mid][0] > timestamp:
                j = mid - 1
            else:
                best = mid
                i = mid + 1
        
        if best is None:
            return ""
        return values[best][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)