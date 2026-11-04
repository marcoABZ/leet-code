class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: list[int]) -> list[int]:
        queue = [([0], numArrows, 0)]
        best, result = 0, None
        
        while queue:
            #print(queue)
            arrows, remaining, score = queue.pop(0)
            if len(arrows) == 12:
                if score > best:
                    arrows[0] = remaining
                    result = arrows
                    best = score
                continue
            
            aArrows = aliceArrows[len(arrows)]
            if remaining > aArrows:
                queue.append((arrows[:] + [aArrows + 1], remaining - aArrows - 1, score + len(arrows)))
            queue.append((arrows[:] + [0], remaining, score))

        return result