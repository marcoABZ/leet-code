class MyStack(object):

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.a:
            self.a.append(x)
            while self.b:
                self.a.append(self.b[0])
                self.b = self.b[1:]
            return
        self.b.append(x)
        while self.a:
            self.b.append(self.a[0])
            self.a = self.a[1:]
        

    def pop(self):
        """
        :rtype: int
        """
        if not self.a and not self.b:
            return None
        if self.a:
            v = self.a[0]
            self.a = self.a[1:]
            return v
        v = self.b[0]
        self.b = self.b[1:]
        return v
        

    def top(self):
        """
        :rtype: int
        """
        if not self.a and not self.b:
            return None
        if self.a:
            return self.a[0]
        return self.b[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.a and not self.b
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()