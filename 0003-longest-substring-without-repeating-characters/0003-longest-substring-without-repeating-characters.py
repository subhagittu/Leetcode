class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l1 = []
        maxlen = 0
        for i in range(0,len(s)):
            l1 = []
            l1.append(s[i])
            maxlen = max(maxlen,len(l1))
            for j in range(i+1,len(s)):
                if s[j] not in l1:
                    l1.append(s[j])
                    maxlen = max(maxlen,len(l1))
                else:
                    break

        return maxlen

              
                
