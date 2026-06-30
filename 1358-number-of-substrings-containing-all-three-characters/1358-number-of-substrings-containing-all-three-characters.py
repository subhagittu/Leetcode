class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastA = lastB = lastC = -1
        total = 0

        for i, ch in enumerate(s):
            if ch == 'a':
                lastA = i
            elif ch == 'b':
                lastB = i
            else:
                lastC = i

            if lastA != -1 and lastB != -1 and lastC != -1:
                total += min(lastA, lastB, lastC) + 1

        return total