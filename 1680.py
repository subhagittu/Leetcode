class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        main1 = ''
        for i in range(1,n+1):
            
            num = i
            binary = bin(num)[2:]
            main1 += binary

        num2 = int(main1,2)
        return num2%(10**9+7)
        
