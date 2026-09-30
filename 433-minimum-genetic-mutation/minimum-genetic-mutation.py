class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        def distance(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
            return diff

        if endGene not in bank:
            return -1
        if distance(startGene, endGene) == 1:
            return 1

        adj = {
            's': [],
            'e': [],
        }

        for i, a in enumerate(bank):
            if distance(a, startGene) <= 1:
                adj['s'].append(i)

            if distance(a, endGene) <= 1:
                if i in adj:
                    adj[i].append('e')
                else:
                    adj[i] = ['e']

            for j, b in enumerate(bank[i+1:]):
                if distance(a, b) == 1:
                    if i in adj:
                        adj[i].append(j+i+1)
                    else:
                        adj[i] = [j+i+1]

                    if j+i+1 in adj:
                        adj[j+i+1].append(i)
                    else:
                        adj[j+i+1] = [i]
        
        queue = [('s', 0)]
        visited = set(['s'])

        while queue:
            curr, steps = queue[0]
            queue = queue[1:]

            if curr == 'e':
                return steps

            if curr not in adj:
                continue

            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps+1))
        
        return -1

        