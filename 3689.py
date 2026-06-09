class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        gMin = gMax = nums[0]

        for n in nums:
            gMin = min(gMin, n)
            gMax = max(gMax, n)

        return (gMax - gMin) * k
