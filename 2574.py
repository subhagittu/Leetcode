class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0,len(nums)):
            leftsum = 0
            rightsum = 0
            rightsum = sum(nums[i+1:len(nums)])
            leftsum = sum(nums[0:i])

            ele1 = abs(leftsum-rightsum)
            res.append(ele1)

        return res
