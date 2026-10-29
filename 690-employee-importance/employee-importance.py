"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mp = {}
        for e in employees:
            mp[e.id] = e
        
        result = 0
        queue = [id]

        while queue:
            c = queue.pop(0)
            result += mp[c].importance
            queue += mp[c].subordinates
        
        return result