class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters.sort()
        n1 = ord(target)
        for ch in letters:
            if ord(ch) > n1:
                return ch
                break
        return letters[0]
