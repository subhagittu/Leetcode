class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        l1 = []
        n = len(words)

        for i in range(0, len(words)):
            if words[i] == target:
                diff = abs(i - startIndex)
                l1.append(abs(min(diff, n - diff)))

        for i in range(0, -len(words)+1, -1):
            if words[i] == target:
                diff = abs(i - startIndex)
                l1.append(abs(min(diff, n - diff)))

        if l1 != []:
            return min(l1)
        else:
            return -1
