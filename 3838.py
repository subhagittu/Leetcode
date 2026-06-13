class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        ans = []
        res = []
        for word in words:
            total = 0
            for char in word:
                num1 = ord(char)-ord('a')
                total += weights[num1]

            totmod = total % 26
            chr1 = chr(ord('z')-totmod)

            res.append(chr1)

        return ''.join(res)

            
