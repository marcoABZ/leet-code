from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colorBalls = dict()
        ballColors = defaultdict(int)
        colors = 0
        result = []

        for ball, color in queries:
            if ballColors[ball] != 0:
                colorBalls[ballColors[ball]].remove(ball)
                if not colorBalls[ballColors[ball]]:
                    del colorBalls[ballColors[ball]]
                    colors -= 1

            if color in colorBalls:
                colorBalls[color].add(ball)
            else:
                colorBalls[color] = set([ball])
                colors += 1

            ballColors[ball] = color
            result.append(colors)
        
        return result