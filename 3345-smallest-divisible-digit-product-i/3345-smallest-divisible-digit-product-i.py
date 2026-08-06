class Solution(object):
    def digsum(self,n):
        res = 1
        while n != 0:
            rem = n%10
            res *= rem
            n = n//10

        return res

    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while n <= 100:
            n1 = self.digsum(n)
            if n1%t == 0:
                return n
            n += 1

