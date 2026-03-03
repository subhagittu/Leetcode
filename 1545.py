class Solution(object):
    def invert(self, s):
        return ''.join('1' if ch == '0' else '0' for ch in s)

    def recur(self, num):
        if num == 1:
            return "0"

        
        inverted = self.invert(self.recur(num - 1))
        return self.recur(num - 1) + "1" + inverted[::-1]

    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        bin1 = ""
        if n == 1:
            bin1 = "0"
        elif n > 1:
            bin1 = self.recur(n)

        return bin1[k-1]




        

        
