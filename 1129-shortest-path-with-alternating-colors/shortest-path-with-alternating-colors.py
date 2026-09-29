class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        answer = [-1] * n

        redAdj = dict()
        for edge in redEdges:
            if edge[0] not in redAdj:
                redAdj[edge[0]] = [edge[1]]
            else:
                redAdj[edge[0]].append(edge[1])
        
        blueAdj = dict()
        for edge in blueEdges:
            if edge[0] not in blueAdj:
                blueAdj[edge[0]] = [edge[1]]
            else:
                blueAdj[edge[0]].append(edge[1])
        
        visited = set([(0,'r'), (0,'b')])
        queue = [(0,0,'r'),(0,0,'b')]

        while queue:
            curr, steps, color = queue[0]
            queue = queue[1:]

            if answer[curr] == -1:
                answer[curr] = steps

            neighbors = blueAdj.get(curr, []) if color == 'r' else redAdj.get(curr, [])
            nextColor = 'b' if color == 'r' else 'r'

            for neighbor in neighbors:
                if (neighbor, nextColor) in visited:
                    continue
                
                visited.add((neighbor, nextColor))
                queue.append((neighbor, steps+1, nextColor))
        
        return answer
        