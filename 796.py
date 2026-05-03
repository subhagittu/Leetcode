class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        s1 = s[:]
        for i in range(0,len(s1)):
            s2 = s1[1:]
            s2 = s2+s1[0]
            if s2 == goal:
                return True
            s1 = s2[:]

        return False


        
