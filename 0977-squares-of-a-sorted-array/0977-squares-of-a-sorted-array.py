class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums1 = []
        for ele in nums:
            nums1.append(ele**2)

        return sorted(nums1)