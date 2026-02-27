class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = int(s,2)
        cnt = 0
        while num >= 1:
            if num%2 == 0:
                num = num//2
                cnt += 1
            if num%2 != 0 and num != 1:
                num += 1
                cnt += 1
            if num == 1:
                return cnt
        #return cnt

        
