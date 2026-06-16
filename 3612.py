class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for char in s:
            if char not in ('#', '%', '*'):
                res += char
            elif char == '#':
                res = res+res
            elif char == '%':
                res = res[::-1]

            elif char == '*':
                n = len(res)
                res = res[0:n-1]


        return res
