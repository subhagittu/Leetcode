class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        s1 = ''
        s2 = ''
        for ele in word1:
            s1 += ele

        for ele in word2:
            s2 += ele

        return s1 == s2

