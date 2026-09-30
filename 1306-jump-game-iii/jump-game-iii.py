class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        visited = set()
        queue = [start]

        while queue:
            curr = queue[0]
            queue = queue[1:]

            if arr[curr] == 0:
                return True
            
            destinations = [curr + arr[curr], curr - arr[curr]]

            for dest in destinations:
                if dest >= 0 and dest < len(arr) and dest not in visited:
                    visited.add(dest)
                    queue.append(dest)
        
        return False