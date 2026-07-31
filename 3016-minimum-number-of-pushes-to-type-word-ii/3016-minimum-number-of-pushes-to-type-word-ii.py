class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = [0]*26

        for ch in word:
            freq[ord(ch)-ord('a')] += 1

        pushcnt = 0
        freq.sort(reverse = True)
        ans = 0
        for i in range(0,26):
            if i%8 == 0:
                pushcnt += 1
            ans += freq[i]*pushcnt


        return ans
