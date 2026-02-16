class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary1 = ""
        for _ in range(0,32):
            binary1 = str(n%2) + binary1
            n = n//2

        binary2 = "".join(reversed(binary1))
        num1 = int(binary2,2)
        return num1
