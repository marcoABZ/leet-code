class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absences = 0
        consecutiveLate = 0

        for c in s:
            if c == 'A':
                absences += 1
                if absences == 2:
                    return False

            if c == 'L':
                consecutiveLate += 1
                if consecutiveLate == 3:
                    return False
            else:
                consecutiveLate = 0
        return True