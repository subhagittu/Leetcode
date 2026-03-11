class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin1 = bin(n)[2:]
        bin2 = ''
        for char in bin1:
            if char == '1':
                bin2 += '0'
            else:
                bin2 += '1'

        n1 = int(bin2,2)
        return n1

        
