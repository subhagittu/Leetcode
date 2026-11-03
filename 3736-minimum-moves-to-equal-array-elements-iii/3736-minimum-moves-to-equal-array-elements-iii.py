class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = max(nums)
        res = 0
        for x in nums:
            res += mx - x
        return res