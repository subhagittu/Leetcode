class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        pushcnt = 0
        ans = 0
        for i in range(0,len(word)):
            if i%8 == 0:
                pushcnt += 1
            ans += 1 * pushcnt

        return ans