class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        flag = True

        for i in range(n):
            if i > 0 and s[i] < s[i - 1]:
                flag = False
                break

        if flag:
            return 0

        if n == 2:
            return -1

        minChar = 'z'
        maxChar = 'a'

        for ch in s:
            minChar = min(minChar, ch)
            maxChar = max(maxChar, ch)

        if minChar == s[0] or maxChar == s[n - 1]:
            return 1

        for i in range(1, n - 1):
            if s[i] == minChar or s[i] == maxChar:
                return 2

        return 3