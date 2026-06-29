class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count = 0
        for s in patterns:
            if word.find(s) != -1: 
                count += 1
        return count