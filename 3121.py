class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        lower_last = {}
        upper_first = {}

        for i, char in enumerate(word):
            if char.islower():
                lower_last[char] = i      # keeps updating → last lowercase
            else:
                if char not in upper_first:
                    upper_first[char] = i   # only first uppercase

        cnt = 0

        for ch in lower_last:
            upper = ch.upper()

            if upper in upper_first:
                if lower_last[ch] < upper_first[upper]:
                    cnt += 1

        return cnt
