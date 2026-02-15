class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a,b = a[::-1], b[::-1]
        res = ''
        carry = 0
        for i in range(0,max(len(a),len(b))):
            digitA = 0
            if i < len(a):
                digitA = ord(a[i]) - ord('0')
            digitB = 0
            if i < len(b):
                digitB = ord(b[i]) - ord('0')

            total = digitA + digitB + carry
            char = str(total%2)
            res = char + res
            carry = total//2

        if carry:
            res = "1" + res
        return res
