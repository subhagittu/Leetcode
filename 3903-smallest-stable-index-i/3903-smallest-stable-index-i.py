class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        min1 = float('inf')

        suffix = [0]*n
        for i in range(n-1,-1,-1):
            min1 = min(min1,nums[i])
            suffix[i] = min1

        max1 = 0

        for i in range(0,n):
            max1 = max(max1,nums[i])
            score = max1-suffix[i]

            if score <= k:
                return i

        return -1

