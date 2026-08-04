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
            if minum in nums:
                minum += 1
                continue
            else:
                l1.append(minum)
            minum += 1

        return l1