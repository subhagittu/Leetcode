class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum((i+1)*(ord('z')-ord(c)+1) for i, c in enumerate(s))