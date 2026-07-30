class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)

        fullGroups = n // 8
        remaining = n % 8
        res = 0
        num1 = 1
        while num1 <= fullGroups:
            res += num1 * 8
            num1 += 1

        res += remaining*num1

        return res