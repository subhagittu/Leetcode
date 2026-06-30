class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num1 = 0
        num2 = 0
        l1 = list(map(int,num))
        for i in range(0,len(l1)):
            if i%2 == 0:
                num1 += l1[i]
            else:
                num2 += l1[i]

        return num1 == num2
