class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        count1 = 0
        n1 = n
        res = ''
        n3 = 0
        while n1 != 0:
            n2 = n1%10
            if n2 != 0:
                res += str(n2)
            n3 += n2
            n1 = n1//10
        res = res[::-1]
        res = int(res) if res else 0
        ans = res*n3

        return ans

