class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        set1 = set()
        for i in range(1,n+1):
            set1.add(i*i)
        count = 0

        for i in range(1,n+1):
            num1 = i*i
            for j in range(i+1,n+1):
                num2 = j*j

                if num1 + num2 in set1:
                    count += 2

        return count
