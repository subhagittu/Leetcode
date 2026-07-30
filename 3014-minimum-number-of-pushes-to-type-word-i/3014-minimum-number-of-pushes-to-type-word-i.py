class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)

        fullGroups = n // 8
        remaining = n % 8

        return (fullGroups * 4 + remaining) * (fullGroups + 1)