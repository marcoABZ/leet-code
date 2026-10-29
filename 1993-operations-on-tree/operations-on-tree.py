from collections import defaultdict

class LockingTree:

    def __init__(self, parent: list[int]):
        self.parent = parent
        self.lockedBy = [None] * len(parent)
        self.desc = defaultdict(list)

        for i, p in enumerate(parent):
            self.desc[p].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.lockedBy[num] is not None:
            return False
        self.lockedBy[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.lockedBy[num] != user:
            return False
        self.lockedBy[num] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.lockedBy[num] is not None:
            return False

        parent = self.parent[num]
        while parent != -1:
            if self.lockedBy[parent] is not None:
                return False
            parent = self.parent[parent]

        queue = self.desc[num][:]
        foundDesc = False    
        while queue:
            curr = queue.pop(0)
            if self.lockedBy[curr] is not None:
                foundDesc = True
                self.lockedBy[curr] = None
            queue += self.desc[curr][:]
        
        if not foundDesc:
            return False
        return self.lock(num, user)
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)