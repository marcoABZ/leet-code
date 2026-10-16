class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        min1 = [60 * int(c[:2]) + int(c[3:]) for c in event1]
        min2 = [60 * int(c[:2]) + int(c[3:]) for c in event2]

        if min1[0] < min2[0]:
            return min1[1] >= min2[0]
        else:
            return min2[1] >= min1[0]