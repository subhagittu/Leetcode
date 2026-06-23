class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        freq = [0]*26
        for i in range(0,len(s)):
            freq[ord(s[i])-ord('a')] += 1
            freq[ord(t[i])-ord('a')] -= 1

        for ele in freq:
            if ele != 0:
                return False

        return True
        
