class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = tally = s.count('a')
        
        for ch in s:

            if ch == 'a':
                tally-= 1
                if tally < ans:
                    ans = tally
            else:
                tally+= 1

        return  ans
        
