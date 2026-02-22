class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = ""
        if n == 0:
            binary = "0"
        else:
            while n > 0:
                binary = str(n%2) + binary
                n = n//2
        i , j = 0, 0
        diff = 0
        for j in range(0,len(binary)):
            if binary[j] == '1':
                diff = max(diff,j-i)
                i = j

        return diff


                

        
        
