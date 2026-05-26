class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        cnt = 0
        seen = set()
        for char in word:
            if char.lower() in word and char.upper() in word:
                if char.lower() not in seen and char.upper() not in seen:
                    cnt += 1
                    seen.add(char.lower())
                    seen.add(char.upper())
        return cnt
