class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = ""
        while n > 0:
            binary = str(n%2) + binary
            n = n//2

        for i in range(1,len(binary)):
            if binary[i] == binary[i-1]:
                return False
        return True
