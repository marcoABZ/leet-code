class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set([0])
        keys = [r for r in rooms[0] if r != 0]

        while keys:
            curr = keys[0]
            keys = keys[1:]
            visited.add(curr)
                
            for k in rooms[curr]:
                if k not in visited:
                    keys.append(k)
        
        for i in range(len(rooms)):
            if i not in visited:
                return False
        return True