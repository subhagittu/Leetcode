class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        prev_zeroes = 0
        curr_zeroes = 0
        total_ones = 0
        i = 0
        best = 0
        while i < n:
            if s[i] == '0':
                prev_zeroes += 1
                i += 1
            else:
                while i < n and s[i] == '1':
                    total_ones += 1
                    i += 1
                while i < n and s[i] == '0':
                    curr_zeroes += 1
                    i += 1
                if prev_zeroes and curr_zeroes:
                    best = max(best,prev_zeroes+curr_zeroes)

                prev_zeroes = curr_zeroes
                curr_zeroes = 0

        return best+total_ones  
