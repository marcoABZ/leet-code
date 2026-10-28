class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        vals = [int(v) for v in s.split(" ") if v.isdigit()]

        v = -1
        for n in vals:
            if n <= v:
                return False
            v = n
        
        return True