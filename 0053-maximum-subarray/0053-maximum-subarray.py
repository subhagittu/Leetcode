class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        total = nums[0]
        for i in range(1,len(nums)):
            if total < 0:
                total = 0
                #maxsum = max(maxsum,total)
            total += nums[i]
            maxsum = max(maxsum, total)

        return maxsum