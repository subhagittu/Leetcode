class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot = nz = 0

        for n in nums:
            nz |= n > 0
            tot ^= n

        return nz * (len(nums) - (not tot))