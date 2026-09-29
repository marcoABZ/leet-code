class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []

        queue = [[0]]
        target = len(graph) - 1
        while queue:
            curr = queue[0]
            queue = queue[1:]

            if curr[-1] == target:
                result.append(curr)
                continue

            for neighbor in graph[curr[-1]]:
                queue.append(curr + [neighbor])
        
        return result

