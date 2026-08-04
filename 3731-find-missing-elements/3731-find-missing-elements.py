class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maxnum = max(nums)
        minum = min(nums)
        l1 = []
        while minum <= maxnum:
            if minum not in nums:
                l1.append(minum)
            
            minum += 1

        return l1