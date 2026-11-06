class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merged = []
        i, j, limit = 0, 0, meetings[0][1]
        while j < len(meetings):
            if meetings[j][0] <= limit:
                limit = max(limit, meetings[j][1])
                j += 1
            else:
                merged.append([meetings[i][0], limit])
                i = j
                limit = meetings[i][1]
        
        merged.append([meetings[i][0], limit])

        j = 1
        result = merged[0][0] - 1
        while j < len(merged):
            result += merged[j][0] - merged[j-1][1] - 1
            j += 1

        result += days - merged[j-1][1]
        return result