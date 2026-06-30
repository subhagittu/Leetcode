class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        def ismatched(word1, chars):
            # d1 = Counter(chars)
            d1 = {}
            for char in chars:
                if char in d1:
                    d1[char] += 1
                else:
                    d1[char] = 1
            for ele in word1:
                if ele not in d1 or d1[ele] <= 0:
                    return False

                d1[ele] -= 1

            return True
        cnt = 0
        for ele in words:
            if ismatched(ele, chars):
                cnt += len(ele)

        return cnt