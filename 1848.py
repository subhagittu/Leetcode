class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        t1 = target
        j = 0
        min1 = float('inf')
        for i in range(0,len(nums)):
            if t1 == nums[i]:
                j = i
                min1 = min(min1, abs(j-start))
                
        if min1 == float('inf'):
            return 0
        else:
            return min1
