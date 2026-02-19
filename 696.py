#from itertools import pairwise
class Solution(object):
    def countBinarySubstrings(self, s):
        prev, cur, cnt = 0, 1, 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                cnt += min(prev, cur)
                prev = cur
                cur = 1

        return cnt + min(prev, cur)
