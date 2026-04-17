class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d1 = {}
        nums.reverse()
        min_dist = float('inf')

        for i, n in enumerate(nums):
            # reverse number
           

            rev = int(str(n)[::-1])

            # check if reverse exists
            if rev in d1:
                min_dist = min(min_dist, abs(i - d1[rev]))
            

            # store current index AFTER checking
            d1[n] = i

        return min_dist if min_dist != float('inf') else -1
