class Solution(object):
    def firstStableIndex(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pmax = -1
        cand = cmax = 0

        for i, x in enumerate(A):
            pmax = max(pmax, x)

            if i == cand:
                cmax = pmax

            if x < cmax - k:
                cand = i + 1

        return cand if cand < len(A) else -1