class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        vals = dict()
        pairs = 0

        for h in hours:
            if (24 - (h % 24)) % 24  in vals:
                pairs += vals[(24 - (h % 24)) % 24]
            
            if h % 24 in vals:
                vals[h % 24] += 1
            else:
                vals[h % 24] = 1

        return pairs