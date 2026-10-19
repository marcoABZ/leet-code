class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        bestArea = 0

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
                for k in range(j+1, len(points)):
                    b = ((points[i][0] - points[k][0])**2 + (points[i][1] - points[k][1])**2)**0.5
                    c = ((points[j][0] - points[k][0])**2 + (points[j][1] - points[k][1])**2)**0.5 
                    if a + b > c and a + c > b and b + c > a:
                        s = (a + b + c) / 2
                        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
                        bestArea = max(bestArea, area)

        return bestArea