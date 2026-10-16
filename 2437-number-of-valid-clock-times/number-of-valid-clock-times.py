class Solution:
    def countTime(self, time: str) -> int:
        result = 1
        for i, c in enumerate(time):
            if c == "?":
                if i == 0:
                    if time[i+1] == "?":
                        result *= 3
                    else:
                        result *= 3 if int(time[i+1]) <= 3 else 2
                elif i == 1:
                    if time[i-1] == "?":
                        result *= 8
                    else:
                        result *= 10 if int(time[i-1]) <= 1 else 4
                elif i == 3:
                    result *= 6
                elif i == 4:
                    result *= 10
        
        return result