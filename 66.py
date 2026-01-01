class Solution(object):
    def plusOne(self, digits):
        """ 
        :type digits: List[int]
        :rtype: List[int]
        """
        s1 = ''
        for i in digits:
            s1 += str(i)
        s1 = int(s1)
        s2 = s1+1
        s2 = str(s2)
        l1 = []
        for i in s2:
            l1.append(int(i))
        return l1
        
