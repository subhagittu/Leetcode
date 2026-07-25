class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1 = n
        l1 = []
        while n1 != 0:
            n2 = n1%10
            l1.append(n2)
            n1 = n1//10

        l1.sort()
        return l1[-1]*l1[-2]