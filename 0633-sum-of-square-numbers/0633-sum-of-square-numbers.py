class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(sqrt(c)) + 1):  
            b = sqrt(c - a * a) 
            if b == int(b):  
                return True  
        return False  