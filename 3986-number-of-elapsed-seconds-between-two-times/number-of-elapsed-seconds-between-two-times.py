class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        hs, ms, ss = startTime.split(":")
        he, me, se = endTime.split(":")

        result, carry = 0, 0
        if int(ss) > int(se):
            result += 60 - int(ss) + int(se)
            carry = 1
        else:
            result += int(se) - int(ss)
        
        if int(ms) > int(me):
            result += 60 * (60 - int(ms) + int(me) - carry)
            carry = 1
        else:
            result += 60 * (int(me) - int(ms) - carry)
            carry = 0
                
        result += 3600 * (int(he) - int(hs) - carry)
        return result