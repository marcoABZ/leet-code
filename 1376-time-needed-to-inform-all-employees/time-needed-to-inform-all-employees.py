class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        adj = dict()
        top = 0

        for i, m in enumerate(manager):
            if m == -1:
                continue

            if m in adj:
                adj[m].append(i)
            else:
                adj[m] = [i]

        queue = [(headID, 0)]
        while queue:
            curr, time = queue[0]
            queue = queue[1:]
            top = max(top, time)

            if informTime[curr] == 0:
                continue
            
            for subordinate in adj[curr]:
                queue.append((subordinate, time+informTime[curr]))
        
        return top