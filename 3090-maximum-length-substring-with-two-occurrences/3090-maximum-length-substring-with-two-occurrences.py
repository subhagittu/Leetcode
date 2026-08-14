class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = l = mask = 0
        
        for r in range(len(s)):
            k = (ord(s[r]) & 31) << 1
            mask += 1 << k
            
            while ((mask >> k) & 3) == 3:
                mask -= 1 << ((ord(s[l]) & 31) << 1)
                l += 1
                
            res = max(res, r - l + 1)
            
        return res