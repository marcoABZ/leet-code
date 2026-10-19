class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        f, t = 0, 0

        for b in bills:
            if b == 5:
                f += 1
            elif b == 10:
                if not f:
                    return False
                f -= 1
                t += 1
            else:
                if t and f:
                    t -= 1
                    f -= 1
                elif f >= 3:
                    f -= 3
                else:
                    return False
        
        return True
                
                    